from taipy.gui import Gui
from taipy import Core
from pages import home

stylekit = {
    "font-family": "Dancing Script"
}

ROUTES = {
    'home': home
}

# Running Application 
if __name__ == '__main__':
    app = Gui()  # Create GUI instance first
    app.add_pages(ROUTES)
    app.run(title="MealMetrics", watermark="MealMetrics", stylekit=stylekit)  # Run the application
    Core().run()  
