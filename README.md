# 3D Globe Annotation App

An interactive 3D globe application with annotation tools built using React, MapboxGL, and Fabric.js.

## Features

- **3D Interactive Globe**: Visualize the Earth in 3D with terrain and atmosphere effects
- **Rich Annotation Tools**: Add markers, text notes, and hyperlinks to the map
- **Interactive Canvas**: Annotations can be moved, edited, and styled
- **Transparent Canvas Overlay**: Fabric.js canvas sits on top of the map with a transparent background
- **State Management**: Zustand for lightweight state management of annotations

## Tech Stack

- **Frontend Framework**: React + TypeScript + Vite
- **Map Visualization**: MapboxGL JS for 3D globe rendering
- **Annotations**: Fabric.js for interactive canvas-based annotations
- **Styling**: Tailwind CSS for utility-first styling
- **State Management**: Zustand for state management

## Getting Started

### Prerequisites

- Node.js and npm installed
- MapboxGL access token (sign up at [mapbox.com](https://www.mapbox.com/))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/globe-annotation-app.git
   cd globe-annotation-app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Add your MapboxGL token:
   Edit `src/components/GlobeMap.tsx` and replace `YOUR_MAPBOX_TOKEN` with your actual token.

4. Start the development server:
   ```bash
   npm run dev
   ```

5. Open your browser and navigate to `http://localhost:5173` (or the URL shown in your terminal).

## Usage

- **Navigate the Globe**: Drag to rotate, scroll to zoom, shift+drag to tilt
- **Add Annotations**: Use the annotation toolbar to add different types of annotations
- **Edit Annotations**: Click on an annotation to select and edit it, drag to move
- **Style Annotations**: Edit text, change colors, and adjust sizes of annotations

## Project Structure

```
/
├── src/
│   ├── components/
│   │   ├── GlobeMap.tsx      # Main 3D globe map component
│   │   └── AnnotationTools.tsx # Annotation controls component
│   ├── store/
│   │   └── annotationStore.ts # Zustand state store for annotations
│   ├── App.tsx               # Main application component
│   └── main.tsx              # Application entry point
├── public/                   # Static assets
└── ...configuration files
```

## Customizing

- **Map Style**: Change the MapboxGL style in `GlobeMap.tsx` for different map appearances
- **Annotation Styles**: Modify Fabric.js options in the annotation creation functions
- **UI**: The interface uses Tailwind CSS classes for easy customization

## License

MIT

## Acknowledgements

- [MapboxGL JS](https://docs.mapbox.com/mapbox-gl-js/api/)
- [Fabric.js](http://fabricjs.com/)
- [React](https://react.dev/)
- [Zustand](https://github.com/pmndrs/zustand)
