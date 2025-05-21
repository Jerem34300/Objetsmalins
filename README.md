# Objets Malins du Quotidien - Automated Passive Income Site

This repository is a fully automated static site for generating passive income via affiliate marketing and ads.

## Setup Instructions

1. **Fork this repository** on GitHub.
2. **Set GitHub Pages** to use the `main` branch and the `/` (root) folder.
3. **Add repository secrets** (Settings > Secrets > Actions):
   - `AMAZON_TAG`: Your Amazon Associates tag (e.g. `tontag-21`)
   - `GOOGLE_ANALYTICS_ID`: Your Google Analytics Tracking ID (e.g. `UA-XXXXXX-X`)
   - `ADSENSE_CLIENT_ID`: Your AdSense client ID (e.g. `ca-pub-XXXXXXXXXXXX`)
   - `OPENAI_API_KEY`: Your OpenAI API key (for post generation)

Once set up, the site will:
- Publish new affiliate content weekly
- Deploy automatically to GitHub Pages
- Contain AdSense & Analytics integration

Enjoy!