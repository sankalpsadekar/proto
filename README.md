# GeoSpatial Annotations API

A FastAPI backend application that provides a comprehensive API for storing and retrieving various types of geospatial annotations.

## Features

- **Spatial Data Management**: Store and query geospatial data with PostgreSQL/PostGIS
- **Multiple Annotation Types**:
  - **Basic Items**: Simple points with name and description
  - **Annotations**: General purpose annotations with JSON content
  - **Note Annotations**: Text notes attached to locations
  - **Link Annotations**: Clickable hyperlinks on the map
  - **Image Annotations**: Images attached to locations with S3 storage

## Tech Stack

- **Backend**: FastAPI & Python 3.8+
- **Database**: PostgreSQL with PostGIS extension
- **ORM**: SQLAlchemy with GeoAlchemy2
- **Media Storage**: AWS S3 for image uploads
- **Migration**: Alembic

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL with PostGIS extension
- AWS account (for S3 image storage)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/geospatial-annotations-api.git
   cd geospatial-annotations-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with:
   ```
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/db_name
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   S3_BUCKET_NAME=your_bucket_name
   AWS_REGION=us-east-1
   ```

5. Run migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Basic Items
- `GET /api/items/` - Get all items
- `POST /api/items/` - Create new item

### Annotations
- `GET /api/annotations/` - Get all annotations
- `POST /api/annotations/` - Create new annotation
- `GET /api/annotations/user/{user_id}` - Get user's annotations

### Note Annotations
- `GET /api/note_annotations/` - Get all note annotations
- `POST /api/note_annotations/` - Create new note annotation
- `GET /api/note_annotations/user/{user_id}` - Get user's note annotations

### Link Annotations
- `GET /api/link_annotations/` - Get all link annotations
- `POST /api/link_annotations/` - Create new link annotation
- `GET /api/link_annotations/user/{user_id}` - Get user's link annotations

### Image Annotations
- `GET /api/image_annotations/` - Get all image annotations
- `POST /api/image_annotations/` - Upload image and create new image annotation
- `GET /api/image_annotations/user/{user_id}` - Get user's image annotations

## API Usage Examples

### Create a Simple Item
```json
POST /api/items/
{
  "name": "Sample Point",
  "description": "This is a sample point on the map",
  "geom": "POINT(30.123 45.678)"
}
```

### Create an Annotation
```json
POST /api/annotations/
{
  "user_id": "user123",
  "type": "point",
  "geometry": "POINT(30.123 45.678)",
  "content": {
    "title": "Test Annotation",
    "description": "This is a test point annotation"
  }
}
```

### Create a Note Annotation
```json
POST /api/note_annotations/
{
  "user_id": "user123",
  "text": "This is a test note",
  "geometry": "POINT(30.123 45.678)",
  "style": {
    "background": "blue",
    "shape": "circle"
  }
}
```

### Create a Link Annotation
```json
POST /api/link_annotations/
{
  "user_id": "user123",
  "name": "Important Resource",
  "description": "Link to documentation",
  "geometry": "POINT(30.123 45.678)",
  "content": {
    "url": "https://example.com/docs"
  },
  "fabric_json": {
    "style": {
      "color": "blue",
      "icon": "link"
    }
  }
}
```

### Create an Image Annotation
```
POST /api/image_annotations/
Content-Type: multipart/form-data

user_id: user123
title: Beautiful Mountain
description: Mountain view from my hike
geometry: POINT(30.123 45.678)
file: [image file]
```

## Database Schema

The application uses PostgreSQL with the PostGIS extension for spatial data. The main tables are:

- `items` - Basic points on the map
- `annotations` - General purpose annotations
- `note_annotations` - Text notes attached to locations
- `link_annotations` - Clickable hyperlinks on the map
- `image_annotations` - Images attached to locations

## Development

### Adding New Features

To add a new annotation type:

1. Create a model in `app/models.py`
2. Add schemas in `app/schemas.py`
3. Add CRUD functions in `app/crud.py`
4. Create a router in `app/routers/`
5. Register the router in `app/main.py`

## Troubleshooting

### Common Issues

- **Geometry Format**: Ensure all geometry data is in proper WKT format (e.g., "POINT(longitude latitude)")
- **Binary Geometry Data**: When retrieving geometry data, make sure to convert EWKB to WKT format to avoid Unicode errors
- **AWS Credentials**: For image uploads, verify that AWS credentials are properly set 