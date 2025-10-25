# 🚀 Vedhify - Quick Start Guide

Get up and running with Vedhify's stunning UI in just 3 steps!

## ⚡ Super Quick Start

```powershell
# 1. Install frontend dependencies
cd UI2
npm install

# 2. Go back to root and start everything
cd ..
.\start_vedhify.ps1
```

That's it! 🎉

## 📋 Prerequisites Check

Before starting, make sure you have:
- ✅ Node.js 18+ installed
- ✅ Python 3.10+ installed
- ✅ Git installed (already done ✓)

## 🎯 Manual Setup (If Script Doesn't Work)

### Terminal 1 - Backend
```powershell
# From root directory (G:\Vedhify)
python app.py
```
✅ Backend will start at http://localhost:5000

### Terminal 2 - Frontend
```powershell
# From root directory
cd UI2
npm run dev
```
✅ Frontend will start at http://localhost:3000

## 🌐 Access the App

Open your browser and go to:
**http://localhost:3000**

## 🎨 What You'll See

1. **Hero Section** - Beautiful animated landing page
   - Floating particles
   - Gradient text
   - Rotating icons
   - Call-to-action buttons

2. **Analysis Interface** - Click "Start Analysis" or scroll down
   - Enter Ayurvedic text
   - Click "Analyze Text" or "Try Demo"
   - Watch stunning animations reveal results

3. **Phytochemical Bridge** - Explore herb-compound relationships
   - Interactive cards
   - Hover effects
   - Detailed information

4. **More Sections** - Sanskrit translator, timeline, and footer

## 🎭 Try the Demo

1. Navigate to the Analysis section
2. Click the **"Try Demo"** button
3. Watch as sample data loads with beautiful animations
4. See herbs, properties, compounds, and AI hypotheses

## 🐛 Troubleshooting

### Port Already in Use?
```powershell
# For port 5000 (Backend)
netstat -ano | findstr :5000
# Kill the process if needed

# For port 3000 (Frontend)
netstat -ano | findstr :3000
```

### Backend Not Responding?
Make sure Flask-CORS is installed:
```powershell
pip install flask-cors
```

### Frontend Build Issues?
```powershell
cd UI2
Remove-Item -Recurse -Force node_modules, .next
npm install
```

## 🎊 You're All Set!

The complete Vedhify experience is now running with:
- ✨ Stunning animations
- 🎨 Modern glassmorphism UI
- 🔄 Seamless transitions
- 🧠 AI-powered analysis
- 📱 Responsive design

**Enjoy exploring Ayurvedic wisdom through modern technology!** 🌿

---

## 📚 Need More Help?

- **Detailed Setup**: See `UI2/README_SETUP.md`
- **Full Documentation**: See `UI2_IMPLEMENTATION_SUMMARY.md`
- **Main README**: See `README.md`
- **GitHub**: https://github.com/Keerthi-Kireeti/Vedhify
