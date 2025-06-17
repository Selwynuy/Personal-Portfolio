"""
Setup script to create the project directory structure.
"""
import os
import shutil
from pathlib import Path

def create_directory_structure():
    # Base directories
    directories = [
        'templates/main',
        'templates/components',
        'static/css',
        'static/js',
        'static/images',
        'media',
        'staticfiles',
    ]

    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

    # Move files from old structure to new structure
    old_static = Path('myportfolio/portfolio/static/portfolio')
    new_static = Path('static')
    
    if old_static.exists():
        # Move CSS files
        for css_file in old_static.glob('css/*'):
            shutil.copy2(css_file, new_static / 'css')
            print(f"Copied CSS file: {css_file}")
        
        # Move JS files
        for js_file in old_static.glob('js/*'):
            shutil.copy2(js_file, new_static / 'js')
            print(f"Copied JS file: {js_file}")
        
        # Move image files
        for img_file in old_static.glob('images/*'):
            shutil.copy2(img_file, new_static / 'images')
            print(f"Copied image file: {img_file}")

    # Move templates
    old_templates = Path('myportfolio/portfolio/templates')
    new_templates = Path('templates')
    
    if old_templates.exists():
        # Move main templates
        for template in old_templates.glob('portfolio/*.html'):
            shutil.copy2(template, new_templates / 'main')
            print(f"Copied template: {template}")
        
        # Move component templates
        for component in old_templates.glob('includes/*.html'):
            shutil.copy2(component, new_templates / 'components')
            print(f"Copied component: {component}")

if __name__ == '__main__':
    create_directory_structure() 