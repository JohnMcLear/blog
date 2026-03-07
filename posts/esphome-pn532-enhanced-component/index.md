---
title: "ESPHome PN532 Enhanced Component"
date: 2026-03-07
tags:
  - "esphome"
  - "nfc"
  - "esp32"
  - "home-assistant"
---

The native ESPHome PN532 component works — until it doesn't. After running PN532 readers over I2C and SPI on ESP32 devices in a real deployment, I hit every known upstream bug: tags flickering on and off while sitting still on the reader, I2C buses hanging after a few hours requiring a power cycle, log spam about blocking operations, and WiFi dropping on nearby ESPs whenever the RF field was on. None of these are edge cases. They're reproducible, long-standing, and have open issues going back years.

So I built a drop-in replacement: [JohnMcLear/esphome_pn532](https://github.com/JohnMcLear/esphome_pn532).

## The Problems It Fixes

**Tag flapping** ([#9875](https://github.com/esphome/esphome/issues/9875)): A card resting on the reader causes alternating `on_tag` / `on_tag_removed` events. The fix is simple — if the same UID is detected again within the removal window, keep it present without triggering an RF cycle.

**I2C freeze** ([#3281](https://github.com/esphome/esphome/issues/3281), [#4745](https://github.com/esphome/esphome/issues/4745)): After a few hours of runtime, the PN532 stops responding on I2C and the only recovery is a power cycle. Fixed with a periodic health check that re-issues `GetFirmwareVersion`. On failure past a configurable threshold, it re-initialises automatically.

**Blocking operation warnings**: `Component pn532 took a long time` flooding the logs indicates the component is blocking the ESPHome event loop. Fixed with exponential backoff (5s → 10s → 60s) after bus failures, so a dead or recovering reader doesn't spam or stall everything else.

**Setup retry**: A single `GetFirmwareVersion` failure at boot marks the component failed permanently in the native implementation. The enhanced version retries twice before giving up.

**WiFi interference** ([PR#1046](https://github.com/esphome/esphome/pull/1046)): The PN532 RF field causes WiFi disconnects on co-located ESP devices. `rf_field_enabled` defaults to `false`, so the field only activates during the poll window.

## Installation

Add to your ESPHome YAML:

```yaml
external_components:
  - source: github://JohnMcLear/esphome_pn532
    components: [pn532, pn532_spi, pn532_i2c]
    refresh: 1d
```

That's it. It's a drop-in replacement — all existing `pn532_spi` / `pn532_i2c` / `pn532` configuration keys still work.

## I2C Configuration

```yaml
i2c:
  sda: GPIO21
  scl: GPIO22

pn532_i2c:
  update_interval: 1s
  health_check_enabled: true
  health_check_interval: 60s
  max_failed_checks: 3
  auto_reset_on_failure: true
  rf_field_enabled: false
  on_tag:
    then:
      - homeassistant.tag_scanned: !lambda 'return x;'

binary_sensor:
  - platform: pn532
    name: "My NFC Tag"
    uid: "74-10-37-94"
```

## SPI Configuration

```yaml
spi:
  clk_pin: GPIO18
  miso_pin: GPIO19
  mosi_pin: GPIO23

pn532_spi:
  cs_pin: GPIO5
  update_interval: 1s
  health_check_enabled: true
  health_check_interval: 60s
  max_failed_checks: 3
  auto_reset_on_failure: true
  rf_field_enabled: false
  on_tag:
    then:
      - logger.log:
          format: "Tag: %s"
          args: ['x.c_str()']
  on_tag_removed:
    then:
      - logger.log:
          format: "Tag removed: %s"
          args: ['x.c_str()']
```

## Finding Your Tag UID

Flash without any binary sensors, open the logs, and scan your tag:

```yaml
pn532_i2c:
  update_interval: 1s
  on_tag:
    then:
      - logger.log:
          format: "Found tag: %s"
          args: ['x.c_str()']
```

You'll see `Found new tag '74-10-37-94'`. Copy that into your `binary_sensor` entry. Both hyphen (`74-10-37-94`) and colon (`74:10:37:94`) formats are accepted.

## What's Supported

ISO14443A cards only for now: Mifare Classic (1k, 4k), Mifare Ultralight / Ultralight C, and the NTAG series (203, 213, 215, 216). Up to two tags per polling cycle.

ISO14443B, FeliCa, and Jewel are physically possible with the PN532 but not yet implemented in the polling logic.

## Counterfeit Modules

Many PN532 modules sold online are clones. They pass the initial version check (reporting Firmware v1.6) but fail during tag polling with I2C/SPI timeouts and `Timed out waiting for readiness` errors. Use genuine Elechouse PN532 modules. If you're getting persistent timeout errors on hardware you trust, the module itself is likely the problem.

The component is at [github.com/JohnMcLear/esphome_pn532](https://github.com/JohnMcLear/esphome_pn532).
