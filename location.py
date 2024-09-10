import tkinter as tk
from tkinter import messagebox
import requests
import folium
import webbrowser
import os

# Function to fetch geolocation info based on IP address
def get_geolocation(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        if data['status'] == 'success':
            location_info = (f"Country: {data['country']}\n"
                             f"Region: {data['regionName']}\n"
                             f"City: {data['city']}\n"
                             f"ZIP: {data['zip']}\n"
                             f"Latitude: {data['lat']}\n"
                             f"Longitude: {data['lon']}")
            return data, location_info
        else:
            return None, "Invalid IP Address or data not found."
    except Exception as e:
        return None, f"Error: {e}"

# Function to handle button click event
def search_location():
    ip_address = ip_entry.get()
    if ip_address:
        data, result = get_geolocation(ip_address)
        if data:
            result_label.config(text=result)
            generate_map(data['lat'], data['lon'], ip_address)
        else:
            result_label.config(text=result)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid IP address.")

# Function to generate the map and open it in a browser
def generate_map(lat, lon, ip_address):
    # Create a map object centered around the given latitude and longitude
    map = folium.Map(location=[lat, lon], zoom_start=10)

    # Add a marker for the location
    folium.Marker([lat, lon], popup=f"IP: {ip_address}").add_to(map)

    # Save the map as an HTML file
    map_file = "geolocation_map.html"
    map.save(map_file)

    # Open the map in the default web browser
    webbrowser.open(f"file://{os.path.abspath(map_file)}")

# GUI Setup
root = tk.Tk()
root.title("Geolocation Tracker")

# IP Input
tk.Label(root, text="Enter IP Address:").pack(pady=5)
ip_entry = tk.Entry(root, width=30)
ip_entry.pack(pady=5)

# Search Button
search_button = tk.Button(root, text="Search Location", command=search_location)
search_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=10)

# Run the application
root.geometry("400x300")
root.mainloop()
