# Deployment Guide

## Deploy to Vercel (Recommended)

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Deploy from Project Directory
```bash
cd /Users/christophermena/Repos/Events-Agent
vercel
```

### 4. Follow the Prompts
- Link to existing project? **No**
- Project name: **events-agent** (or your preferred name)
- Directory: **./** (current directory)
- Override settings? **No**

### 5. Set Environment Variables
After deployment, set your environment variables in the Vercel dashboard:

```bash
# Go to your project dashboard
vercel dashboard

# Or set via CLI
vercel env add SMTP_HOST
vercel env add SMTP_PORT
vercel env add SMTP_USER
vercel env add SMTP_PASSWORD
vercel env add RECIPIENT
vercel env add SENDER_NAME
vercel env add FACEBOOK_ACCESS_TOKEN
vercel env add FACEBOOK_PAGE_IDS
```

### 6. Redeploy
```bash
vercel --prod
```

## Alternative: Deploy to Railway

### 1. Install Railway CLI
```bash
npm install -g @railway/cli
```

### 2. Login and Deploy
```bash
railway login
railway init
railway up
```

## Alternative: Deploy to Heroku

### 1. Create Procfile
```bash
echo "web: python events-bot/app.py" > Procfile
```

### 2. Deploy
```bash
heroku create your-app-name
git push heroku main
```

## Environment Variables for Production

Make sure to set these in your deployment platform:

```bash
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your.email@gmail.com
SMTP_PASSWORD=your_app_password
RECIPIENT=christopher.mena@icloud.com
SENDER_NAME=Reno Family Events Bot

# Source toggles
SOURCE_VISIT_CARSON_CITY=1
SOURCE_PBS_RENO=1
SOURCE_LAKE_TAHOE_TRAVEL=1
# ... etc

# Optional Facebook
FACEBOOK_ACCESS_TOKEN=your_token
FACEBOOK_PAGE_IDS=page_id_1,page_id_2
```

## Troubleshooting

### Vercel Issues
- Make sure `vercel.json` is in the root directory
- Check that `requirements.txt` includes all dependencies
- Verify environment variables are set in Vercel dashboard

### Common Errors
- **404 errors**: Check that routes are properly configured
- **Import errors**: Ensure all dependencies are in requirements.txt
- **Environment errors**: Verify all required env vars are set

## Custom Domain (Optional)

### Vercel
1. Go to your project dashboard
2. Click "Domains"
3. Add your custom domain
4. Update DNS records as instructed

### Railway
1. Go to project settings
2. Click "Domains"
3. Add custom domain
4. Update DNS records
