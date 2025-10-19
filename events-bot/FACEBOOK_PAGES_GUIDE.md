# Finding Local Facebook Page IDs for Family Events

## ✅ Your Facebook Token is Working!

Your Facebook access token is valid and working perfectly. Now we need to find the page IDs for local Reno/Sparks venues that host family events.

## How to Find Facebook Page IDs

### Method 1: Using Facebook Graph API Explorer (Recommended)

1. **Go to Graph API Explorer**: https://developers.facebook.com/tools/explorer/
2. **Select your app** (ID: 2281441722303010)
3. **Use your access token** (it should already be loaded)
4. **Search for local pages** using these queries:

```
Search for "The Discovery":
/search?q=The Discovery Nevada&type=page

Search for "Nevada Museum of Art":
/search?q=Nevada Museum of Art Reno&type=page

Search for "PBS Reno":
/search?q=PBS Reno&type=page

Search for "Washoe County Library":
/search?q=Washoe County Library&type=page

Search for "City of Reno":
/search?q=City of Reno Nevada&type=page

Search for "City of Sparks":
/search?q=City of Sparks Nevada&type=page
```

5. **Copy the page IDs** from the results
6. **Test events access** by trying: `/{page_id}/events`

### Method 2: Direct Page URLs

Visit these Facebook pages and look for the page ID in the URL or page info:

- **The Discovery**: https://www.facebook.com/nvdm.org
- **Nevada Museum of Art**: https://www.facebook.com/nevadaart
- **PBS Reno**: https://www.facebook.com/pbsreno
- **Washoe County Library**: https://www.facebook.com/washoecountylibrary
- **City of Reno**: https://www.facebook.com/cityofreno
- **City of Sparks**: https://www.facebook.com/cityofsparks
- **Reno Public Market**: https://www.facebook.com/renopublicmarket
- **Macaroni KID Reno/Sparks**: Search for "Macaroni KID Reno Sparks"
- **Nevada Moms**: Search for "Nevada Moms"

### Method 3: Using Page Info

1. Go to any Facebook page
2. Click "About" 
3. Scroll down to find the "Page ID" (it's a long number)
4. Or look in the page URL: `facebook.com/pages/Page-Name/{PAGE_ID}`

## Adding Page IDs to Your Agent

Once you have page IDs, update your `.env` file:

```bash
FACEBOOK_PAGE_IDS=page_id_1,page_id_2,page_id_3
```

For example:
```bash
FACEBOOK_PAGE_IDS=123456789012345,987654321098765,555666777888999
```

## Testing Your Setup

After adding page IDs, test with:
```bash
python3 event_agent.py
```

Look for log messages like:
```
INFO Collecting from: Facebook Events (3 pages)
```

## Common Local Venues to Check

### Museums & Educational
- The Discovery (Nevada Discovery Museum)
- Nevada Museum of Art
- National Automobile Museum
- Terry Lee Wells Nevada Discovery Museum

### Libraries & Community
- Washoe County Library
- Reno Public Library
- Sparks Library
- Nevada Moms
- Macaroni KID Reno/Sparks

### Government & Parks
- City of Reno
- City of Sparks
- Washoe County
- Reno Parks and Recreation
- Sparks Parks and Recreation

### Media & Organizations
- PBS Reno
- KUNR (NPR)
- This Is Reno
- Reno News & Review

### Venues & Markets
- Reno Public Market
- The Row (casino properties often have family events)
- Atlantis Casino Resort Spa
- Peppermill Resort Spa Casino

## Pro Tips

1. **Start with 3-5 pages** to test, then add more
2. **Check if pages have events** before adding them
3. **Some pages may not allow public event access** - that's normal
4. **Focus on pages that regularly post family events**
5. **You can always add/remove page IDs** as you discover new venues

## Need Help?

If you find a page but can't access its events, it might be:
- Private or restricted
- Not posting public events
- Requiring special permissions

Just skip those and focus on pages that work!
