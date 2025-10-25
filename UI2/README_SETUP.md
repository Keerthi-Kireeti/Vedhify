# Vedhify UI2 - Setup Guide

## 🚀 Quick Start

This is the main UI for the Vedhify project - a beautiful, modern interface for Ayurvedic text analysis with seamless animations.

### Prerequisites

- Node.js 18+ or Bun
- Python 3.10+ (for backend)

### Installation

1. **Install dependencies:**

```bash
# Using npm
npm install

# Or using bun (faster)
bun install
```

2. **Set up environment variables:**

The `.env.local` file is already created with:
```
NEXT_PUBLIC_API_URL=http://localhost:5000
```

3. **Start the backend (Flask API):**

In a separate terminal, from the root `Vedhify` directory:

```bash
# Activate virtual environment (if using one)
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate

# Start the Flask backend
python app.py
```

The backend should start at `http://localhost:5000`

4. **Start the frontend (Next.js):**

```bash
# Using npm
npm run dev

# Or using bun
bun dev
```

The frontend should start at `http://localhost:3000`

### 🎨 Features

- **Hero Section** - Stunning animated landing with gradient text and particles
- **AI Analysis Interface** - Real-time Ayurvedic text analysis with beautiful results display
- **Phytochemical Bridge** - Interactive cards showing herb-compound relationships
- **Sanskrit Translator** - Translate and explore Ayurvedic terms
- **Timeline** - Historical journey through Ayurveda
- **Seamless Animations** - Powered by Framer Motion with smooth transitions
- **Glassmorphism UI** - Modern design with backdrop blur and gradient effects
- **Toast Notifications** - Real-time feedback for user actions
- **Responsive Design** - Works perfectly on all devices

### 🛠️ Tech Stack

- **Framework:** Next.js 15 with React 19
- **Animations:** Framer Motion
- **Styling:** Tailwind CSS 4
- **UI Components:** Radix UI primitives
- **Icons:** Lucide React
- **3D Graphics:** React Three Fiber (for advanced visualizations)
- **API Integration:** Custom fetch-based API service

### 📁 Project Structure

```
UI2/
├── src/
│   ├── app/                 # Next.js app directory
│   │   ├── page.tsx        # Main page with all sections
│   │   ├── layout.tsx      # Root layout with providers
│   │   └── globals.css     # Global styles and animations
│   ├── components/          # React components
│   │   ├── Navigation.tsx
│   │   ├── HeroSection.tsx
│   │   ├── AnalysisInterface.tsx  # Main analysis component
│   │   ├── PhytochemicalBridge.tsx
│   │   ├── SanskritTranslator.tsx
│   │   ├── Timeline.tsx
│   │   ├── Footer.tsx
│   │   └── ui/             # Reusable UI components
│   ├── lib/
│   │   ├── api.ts          # API service for backend integration
│   │   └── utils.ts        # Utility functions
│   └── hooks/
│       └── use-toast.ts    # Toast notification hook
├── public/                  # Static assets
├── next.config.ts          # Next.js configuration
└── package.json            # Dependencies

```

### 🎯 Usage

1. **Navigate to Home** - See the beautiful hero section with animated background
2. **Click "Start Analysis"** - Scroll to the analysis interface
3. **Enter Text** - Type or paste Ayurvedic text
4. **Analyze** - Click "Analyze Text" to process
5. **View Results** - See herbs, properties, compounds, and AI-generated hypotheses with stunning animations

**Try the Demo:**
- Click "Try Demo" button to load sample data and see the full analysis flow

### 🎨 Customization

**Colors:**
Edit `src/app/globals.css` to customize the color scheme:
- `--primary`: Main brand color
- `--accent`: Secondary accent color
- `--background`: Background color
- `--foreground`: Text color

**Animations:**
All animations are powered by Framer Motion. Edit component files to customize:
- Timing: `duration` property
- Easing: `ease` property
- Delays: `delay` property

### 🐛 Troubleshooting

**Backend Connection Issues:**
- Ensure Flask backend is running on port 5000
- Check `.env.local` has correct API URL
- Verify CORS is enabled in Flask app

**Build Errors:**
- Run `npm install` or `bun install` again
- Delete `node_modules` and `.next` folders, then reinstall
- Check Node.js version (18+)

**Animation Performance:**
- Reduce number of particle effects in components
- Disable some animations on lower-end devices
- Use `will-change` CSS property sparingly

### 📝 Development

**Add New Components:**
```bash
# Create in src/components/
touch src/components/YourComponent.tsx
```

**Add New API Endpoints:**
Edit `src/lib/api.ts` to add new API functions

**Add New Routes:**
Next.js uses file-based routing in `src/app/`

### 🚢 Deployment

**Build for production:**
```bash
npm run build
# or
bun run build
```

**Start production server:**
```bash
npm start
# or
bun start
```

### 📄 License

MIT License - See LICENSE file for details

### 🙏 Credits

Built with ❤️ using:
- Next.js
- Framer Motion
- Tailwind CSS
- Radix UI
- React Three Fiber

---

**Need Help?** Open an issue on GitHub or check the main project README.md
