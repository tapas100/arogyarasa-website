#!/usr/bin/env bash
set -e
# Build the Next.js app
cd frontend
npm install --silent
npm run build --silent
# Deploy placeholder – replace with your deployment platform commands
# Example for Vercel (requires VERCEL_TOKEN env var):
# npx vercel --prod --confirm
# For now we just indicate the build succeeded.
echo "Build completed. Deploy manually using your preferred platform (Vercel, Netlify, etc.)."
