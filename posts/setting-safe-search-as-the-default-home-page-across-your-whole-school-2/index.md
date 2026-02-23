---
title: "Setting Safe Search as the default home page across your whole school"
date: 2011-06-23
categories: 
  - "ict"
  - "primary-school-ict"
  - "primary-school-ict-safe-search"
  - "primary-schools"
  - "primary-schools-ict"
  - "primary-technology"
  - "safe-search"
---

**Creating a Group Policy Object (GPO) to set Safe Search as your Homepage**

1. Open **Group Policy Management Console** – It is found under **Administrative Tools** on the server Start Menu

[![clip_image002](images/clip_image002_thumb.jpg "clip_image002")](http://blog.primaryt.co.uk/files/2011/06/clip_image002.jpg)

1. Right click on **Group Policy Objects** and select **New**

[![clip_image004](images/clip_image004_thumb1.jpg "clip_image004")](http://blog.primaryt.co.uk/files/2011/06/clip_image0041.jpg)

1. Name the policy “**Users – Set Homepage**” – This will be a user policy rather than a computer policy, using a meaningful description will help administration later on.

[![clip_image006](images/clip_image006_thumb.jpg "clip_image006")](http://blog.primaryt.co.uk/files/2011/06/clip_image006.jpg)

1. **Right click** on the policy and select **Edit**. The Group Policy Editor will now open.

[![clip_image008](images/clip_image008_thumb.jpg "clip_image008")](http://blog.primaryt.co.uk/files/2011/06/clip_image008.jpg)

1. Browse through the tree structure to display I**mportant URLs** in the right hand side of the browser

**User Configuration > Windows Settings > Internet Explorer Maintenance > URLs**

[![clip_image010](images/clip_image010_thumb.jpg "clip_image010")](http://blog.primaryt.co.uk/files/2011/06/clip_image010.jpg)

1. **Right click** on **Important URLs** and select **Properties**

Enter the following address for the homepage URL into the dialogue box

[Http://www.primaryschoolict.com](http://www.primaryschoolict.com)

[![clip_image012](images/clip_image012_thumb.jpg "clip_image012")](http://blog.primaryt.co.uk/files/2011/06/clip_image012.jpg)

1. Click on **Ok** and close the **Group Policy Editor**

1. Within the **Group Policy Management** Window browse to the Organisational Unit containing your school users

1. **Right click** on the Organisation Unit and select **Link an existing GPO.**

[![clip_image014](images/clip_image014_thumb.jpg "clip_image014")](http://blog.primaryt.co.uk/files/2011/06/clip_image014.jpg)

1. Select your new GPO from the list and click **Ok**

[![clip_image016](images/clip_image016_thumb.jpg "clip_image016")](http://blog.primaryt.co.uk/files/2011/06/clip_image016.jpg)

1. Your new GPO is now linked and will be applied to the users contained within the Organisational Unit you selected

[![clip_image018](images/clip_image018_thumb1.jpg "clip_image018")](http://blog.primaryt.co.uk/files/2011/06/clip_image0181.jpg)

[](http://blog.primaryt.co.uk/files/2011/06/clip_image0181.jpg)  
**Please be aware if you have another GPO applied at a higher level, for example in the Default Domain Policy settings may not be applied as anticipated. This can happen if you have two conflicting GPO’s. For example if you have two policies to set the homepage, one using www.bbc.co.uk and another using [www.google.co.uk](http://www.google.co.uk/), one of the setting will take precedence.**
