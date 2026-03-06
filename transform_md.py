import os
import re

def transform_md_files():
    processed_count = 0
    # Walk through the current directory and all subdirectories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == 'index.md':
                md_path = os.path.join(root, file)
                
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Regex to find escaped \[code\]...\[/code\] and replace with fenced code blocks
                transformed_content = re.sub(
                    r'\[code\]\s*(.*?)\s*\[/code\]', # Match escaped brackets
                    r'

```
\1
```

',
                    content,
                    flags=re.DOTALL
                )
                
                if transformed_content != content:
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(transformed_content)
                    processed_count += 1
                    print(f"Transformed {md_path}")
    print(f"Processed {processed_count} Markdown files for [code] tags.")

if __name__ == "__main__":
    transform_md_files()
