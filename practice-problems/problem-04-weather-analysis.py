"""
Practice Problem 04: Weather Data Analysis System
===============================================

DIFFICULTY: Intermediate ⭐⭐
CONCEPTS: Arrays, Data Processing, Statistics, File Simulation
ASSIGNMENTS: 5 (Functions), 6 (Arrays/Strings), 7 (2D Arrays)
ESTIMATED TIME: 70-85 minutes

PROBLEM DESCRIPTION:
===================
Create a comprehensive weather data analysis system that processes meteorological
data, calculates statistics, identifies trends, and generates weather reports.
The system should handle multiple weather stations, different measurement types,
and provide detailed analytical insights.

This problem combines data processing, statistical analysis, array manipulation,
and scientific computing concepts to create a practical meteorological tool.

REQUIREMENTS:
============
1. Store and manage weather data for multiple stations
2. Calculate comprehensive weather statistics
3. Identify weather patterns and trends
4. Generate detailed weather reports
5. Compare data between different time periods
6. Handle extreme weather event detection
7. Provide data visualization through text-based charts
8. Include weather prediction based on historical patterns

LEARNING OBJECTIVES:
===================
- Master multi-dimensional array processing
- Understand statistical analysis and data science concepts
- Practice data validation and error handling
- Implement scientific calculation algorithms
- Design professional data analysis systems
- Work with time series data and trends

STARTER CODE:
============
"""

import random
import math
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional

class WeatherStation:
    """Represents a weather monitoring station."""
    
    def __init__(self, station_id: str, name: str, latitude: float, longitude: float):
        """Initialize weather station with location data."""
        self.station_id = station_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.data_points = []  # List of weather measurements
    
    def add_measurement(self, timestamp: str, temperature: float, humidity: float, 
                       pressure: float, wind_speed: float, wind_direction: int, 
                       precipitation: float):
        """Add a weather measurement to the station."""
        measurement = {
            'timestamp': timestamp,
            'temperature': temperature,      # Celsius
            'humidity': humidity,           # Percentage (0-100)
            'pressure': pressure,           # hPa (hectopascals)
            'wind_speed': wind_speed,       # km/h
            'wind_direction': wind_direction,  # Degrees (0-360)
            'precipitation': precipitation   # mm
        }
        self.data_points.append(measurement)

class WeatherAnalysisSystem:
    """Comprehensive weather data analysis and reporting system."""
    
    def __init__(self):
        """Initialize the weather analysis system."""
        self.stations = {}  # Dictionary of weather stations
        self.weather_types = ['temperature', 'humidity', 'pressure', 'wind_speed', 'precipitation']
        
        # Weather condition thresholds
        self.thresholds = {
            'hot_temperature': 35.0,
            'cold_temperature': -10.0,
            'high_humidity': 80.0,
            'low_humidity': 20.0,
            'high_pressure': 1025.0,
            'low_pressure': 995.0,
            'high_wind': 50.0,
            'heavy_rain': 25.0,
            'extreme_rain': 50.0
        }
        
        # Initialize with sample stations
        self.initialize_sample_stations()
    
    def initialize_sample_stations(self):
        """Initialize the system with sample weather stations."""
        stations_data = [
            ("WS001", "Downtown Metropolis", 40.7128, -74.0060),
            ("WS002", "Airport Station", 40.6895, -74.1745),
            ("WS003", "Coastal Observatory", 40.5795, -74.1502),
            ("WS004", "Mountain Peak", 40.9176, -74.1687),
            ("WS005", "University Campus", 40.7589, -73.9851)
        ]
        
        for station_id, name, lat, lon in stations_data:
            self.stations[station_id] = WeatherStation(station_id, name, lat, lon)
        
        # Generate sample data for demonstration
        self.generate_sample_data()
    
    def generate_sample_data(self):
        """Generate realistic sample weather data for all stations."""
        import datetime
        
        # Generate data for the last 30 days
        end_date = datetime.datetime.now()
        start_date = end_date - timedelta(days=30)
        
        for station in self.stations.values():
            current_date = start_date
            
            # Base conditions for each station (simulating different climates)
            base_temp = 15 + random.uniform(-5, 5)  # Base temperature for station
            
            while current_date <= end_date:
                # Generate realistic weather data with some randomness and patterns
                
                # Temperature with seasonal and daily variation
                day_of_year = current_date.timetuple().tm_yday
                seasonal_temp = base_temp + 10 * math.sin((day_of_year - 80) * 2 * math.pi / 365)
                daily_variation = 5 * math.sin((current_date.hour - 14) * math.pi / 12)
                temperature = seasonal_temp + daily_variation + random.uniform(-3, 3)
                
                # Humidity (inverse relationship with temperature)
                humidity = min(100, max(0, 70 - (temperature - 20) * 1.5 + random.uniform(-15, 15)))
                
                # Pressure (varies with weather systems)
                pressure = 1013 + random.uniform(-20, 20) + 5 * math.sin(day_of_year * 2 * math.pi / 10)
                
                # Wind speed
                wind_speed = abs(random.uniform(0, 30) + 5 * math.sin(day_of_year * 2 * math.pi / 7))
                
                # Wind direction
                wind_direction = random.randint(0, 360)
                
                # Precipitation (more likely with low pressure and high humidity)
                precip_chance = (100 - pressure + humidity - 1013) / 100
                if random.random() < max(0, precip_chance):
                    precipitation = random.uniform(0.1, 20)
                    if random.random() < 0.1:  # 10% chance of heavy rain
                        precipitation += random.uniform(20, 50)
                else:
                    precipitation = 0.0
                
                # Add measurement every 3 hours
                for hour_offset in range(0, 24, 3):
                    timestamp_str = (current_date + timedelta(hours=hour_offset)).strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Add some hourly variation
                    hourly_temp = temperature + random.uniform(-2, 2)
                    hourly_humidity = max(0, min(100, humidity + random.uniform(-10, 10)))
                    hourly_pressure = pressure + random.uniform(-2, 2)
                    hourly_wind = max(0, wind_speed + random.uniform(-5, 5))
                    hourly_precip = max(0, precipitation + random.uniform(-1, 1)) if precipitation > 0 else 0
                    
                    station.add_measurement(
                        timestamp_str, hourly_temp, hourly_humidity, 
                        hourly_pressure, hourly_wind, wind_direction, hourly_precip
                    )
                
                current_date += timedelta(days=1)
    
    def display_main_menu(self):
        """Display the main menu options."""
        print("=" * 60)
        print("           WEATHER ANALYSIS SYSTEM")
        print("=" * 60)
        print("1. Station Information & Status")
        print("2. Current Weather Conditions")
        print("3. Statistical Analysis")
        print("4. Weather Trends & Patterns")
        print("5. Extreme Weather Events")
        print("6. Comparative Analysis")
        print("7. Weather Reports")
        print("8. Data Visualization")
        print("9. Weather Prediction")
        print("10. System Administration")
        print("0. Exit")
        print("=" * 60)
    
    def get_menu_choice(self):
        """Get and validate user's menu choice."""
        while True:
            try:
                choice = int(input("Enter your choice (0-10): "))
                if 0 <= choice <= 10:
                    return choice
                else:
                    print("❌ Please enter a number between 0 and 10.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def display_station_information(self):
        """Display comprehensive information about all weather stations."""
        print("\n🌐 WEATHER STATION NETWORK")
        print("-" * 40)
        
        if not self.stations:
            print("❌ No weather stations configured!")
            return
        
        print(f"Total Stations: {len(self.stations)}")
        print()
        
        for station in self.stations.values():
            data_count = len(station.data_points)
            latest_reading = None
            
            if station.data_points:
                latest_reading = max(station.data_points, key=lambda x: x['timestamp'])
            
            print(f"📡 {station.name} ({station.station_id})")
            print(f"   Location: {station.latitude:.4f}°N, {station.longitude:.4f}°W")
            print(f"   Data Points: {data_count:,}")
            
            if latest_reading:
                print(f"   Last Update: {latest_reading['timestamp']}")
                print(f"   Status: ✅ Active")
            else:
                print(f"   Status: ❌ No Data")
            
            print()
        
        # Show data coverage statistics
        self.show_data_coverage_stats()
    
    def show_data_coverage_stats(self):
        """Show statistics about data coverage across all stations."""
        if not self.stations:
            return
        
        print("📊 DATA COVERAGE STATISTICS")
        print("-" * 35)
        
        total_measurements = sum(len(station.data_points) for station in self.stations.values())
        
        if total_measurements == 0:
            print("❌ No measurement data available")
            return
        
        # Find date range
        all_timestamps = []
        for station in self.stations.values():
            for measurement in station.data_points:
                all_timestamps.append(measurement['timestamp'])
        
        if all_timestamps:
            earliest = min(all_timestamps)
            latest = max(all_timestamps)
            print(f"Data Range: {earliest} to {latest}")
        
        print(f"Total Measurements: {total_measurements:,}")
        print(f"Average per Station: {total_measurements / len(self.stations):.1f}")
        
        # Quality metrics
        complete_records = 0
        for station in self.stations.values():
            for measurement in station.data_points:
                if all(measurement[field] is not None for field in self.weather_types):
                    complete_records += 1
        
        completion_rate = (complete_records / total_measurements * 100) if total_measurements > 0 else 0
        print(f"Data Completeness: {completion_rate:.1f}%")
    
    def show_current_conditions(self):
        """Display current weather conditions for all stations."""
        print("\n🌤️  CURRENT WEATHER CONDITIONS")
        print("-" * 40)
        
        if not self.stations:
            print("❌ No weather stations available!")
            return
        
        current_conditions = []
        
        for station in self.stations.values():
            if not station.data_points:
                continue
            
            # Get the most recent measurement
            latest = max(station.data_points, key=lambda x: x['timestamp'])
            current_conditions.append((station, latest))
        
        if not current_conditions:
            print("❌ No current weather data available!")
            return
        
        # Display current conditions
        for station, conditions in current_conditions:
            print(f"📍 {station.name}")
            print(f"   Time: {conditions['timestamp']}")
            print(f"   🌡️  Temperature: {conditions['temperature']:.1f}°C")
            print(f"   💧 Humidity: {conditions['humidity']:.1f}%")
            print(f"   📊 Pressure: {conditions['pressure']:.1f} hPa")
            print(f"   💨 Wind: {conditions['wind_speed']:.1f} km/h @ {conditions['wind_direction']}°")
            print(f"   🌧️  Precipitation: {conditions['precipitation']:.1f} mm")
            
            # Add weather description
            description = self.get_weather_description(conditions)
            print(f"   📝 Conditions: {description}")
            print()
        
        # Show network summary
        self.show_network_summary(current_conditions)
    
    def get_weather_description(self, conditions):
        """Generate descriptive weather conditions based on measurements."""
        temp = conditions['temperature']
        humidity = conditions['humidity']
        wind = conditions['wind_speed']
        precip = conditions['precipitation']
        pressure = conditions['pressure']
        
        descriptions = []
        
        # Temperature descriptions
        if temp >= 35:
            descriptions.append("Very Hot")
        elif temp >= 25:
            descriptions.append("Hot")
        elif temp >= 15:
            descriptions.append("Mild")
        elif temp >= 5:
            descriptions.append("Cool")
        elif temp >= -5:
            descriptions.append("Cold")
        else:
            descriptions.append("Very Cold")
        
        # Precipitation
        if precip >= 50:
            descriptions.append("Extreme Rain")
        elif precip >= 25:
            descriptions.append("Heavy Rain")
        elif precip >= 5:
            descriptions.append("Moderate Rain")
        elif precip > 0:
            descriptions.append("Light Rain")
        
        # Wind
        if wind >= 50:
            descriptions.append("Very Windy")
        elif wind >= 30:
            descriptions.append("Windy")
        elif wind >= 15:
            descriptions.append("Breezy")
        
        # Humidity
        if humidity >= 80:
            descriptions.append("Very Humid")
        elif humidity <= 20:
            descriptions.append("Very Dry")
        
        return ", ".join(descriptions) if descriptions else "Fair"
    
    def show_network_summary(self, current_conditions):
        """Show summary statistics for the entire weather network."""
        if not current_conditions:
            return
        
        print("🌍 NETWORK SUMMARY")
        print("-" * 25)
        
        temps = [c[1]['temperature'] for c in current_conditions]
        humidities = [c[1]['humidity'] for c in current_conditions]
        pressures = [c[1]['pressure'] for c in current_conditions]
        
        print(f"Temperature Range: {min(temps):.1f}°C to {max(temps):.1f}°C")
        print(f"Average Temperature: {sum(temps)/len(temps):.1f}°C")
        print(f"Average Humidity: {sum(humidities)/len(humidities):.1f}%")
        print(f"Average Pressure: {sum(pressures)/len(pressures):.1f} hPa")
        
        # Count stations with precipitation
        precip_stations = sum(1 for c in current_conditions if c[1]['precipitation'] > 0)
        print(f"Stations with Precipitation: {precip_stations}/{len(current_conditions)}")
    
    def perform_statistical_analysis(self):
        """Perform comprehensive statistical analysis of weather data."""
        print("\n📈 STATISTICAL ANALYSIS")
        print("-" * 30)
        
        if not self.stations:
            print("❌ No weather data available!")
            return
        
        print("Select analysis type:")
        print("1. Overall Statistics")
        print("2. Station-Specific Analysis")
        print("3. Parameter Comparison")
        print("4. Time Series Analysis")
        print("5. Correlation Analysis")
        
        try:
            choice = int(input("Enter choice (1-5): "))
            
            if choice == 1:
                self.show_overall_statistics()
            elif choice == 2:
                self.show_station_statistics()
            elif choice == 3:
                self.show_parameter_comparison()
            elif choice == 4:
                self.show_time_series_analysis()
            elif choice == 5:
                self.show_correlation_analysis()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def show_overall_statistics(self):
        """Show comprehensive statistics for all weather data."""
        print("\n📊 OVERALL WEATHER STATISTICS")
        print("-" * 35)
        
        # Collect all data points
        all_data = []
        for station in self.stations.values():
            all_data.extend(station.data_points)
        
        if not all_data:
            print("❌ No data available for analysis!")
            return
        
        print(f"Total Data Points: {len(all_data):,}")
        print(f"Data Collection Period: {self.get_date_range(all_data)}")
        print()
        
        # Calculate statistics for each parameter
        for param in self.weather_types:
            values = [d[param] for d in all_data if d[param] is not None]
            
            if not values:
                continue
            
            stats = self.calculate_statistics(values)
            units = self.get_parameter_units(param)
            
            print(f"📊 {param.title().replace('_', ' ')} ({units})")
            print(f"   Mean: {stats['mean']:.2f}")
            print(f"   Median: {stats['median']:.2f}")
            print(f"   Range: {stats['min']:.2f} to {stats['max']:.2f}")
            print(f"   Std Dev: {stats['std_dev']:.2f}")
            print(f"   Samples: {stats['count']:,}")
            print()
        
        # Show extreme weather events summary
        self.show_extreme_events_summary(all_data)
    
    def calculate_statistics(self, values):
        """Calculate comprehensive statistics for a list of values."""
        if not values:
            return {}
        
        values = sorted(values)
        n = len(values)
        
        stats = {
            'count': n,
            'min': min(values),
            'max': max(values),
            'mean': sum(values) / n,
            'median': values[n//2] if n % 2 == 1 else (values[n//2-1] + values[n//2]) / 2
        }
        
        # Calculate standard deviation
        mean = stats['mean']
        variance = sum((x - mean) ** 2 for x in values) / n
        stats['std_dev'] = math.sqrt(variance)
        
        # Calculate percentiles
        stats['q1'] = values[n//4]
        stats['q3'] = values[3*n//4]
        
        return stats
    
    def get_parameter_units(self, parameter):
        """Get the units for a weather parameter."""
        units = {
            'temperature': '°C',
            'humidity': '%',
            'pressure': 'hPa',
            'wind_speed': 'km/h',
            'precipitation': 'mm'
        }
        return units.get(parameter, '')
    
    def get_date_range(self, data_points):
        """Get the date range for a collection of data points."""
        if not data_points:
            return "No data"
        
        timestamps = [d['timestamp'] for d in data_points]
        return f"{min(timestamps)} to {max(timestamps)}"
    
    def show_extreme_events_summary(self, all_data):
        """Show summary of extreme weather events."""
        print("⚠️  EXTREME WEATHER EVENTS")
        print("-" * 30)
        
        events = {
            'hot_days': sum(1 for d in all_data if d['temperature'] > self.thresholds['hot_temperature']),
            'cold_days': sum(1 for d in all_data if d['temperature'] < self.thresholds['cold_temperature']),
            'high_wind': sum(1 for d in all_data if d['wind_speed'] > self.thresholds['high_wind']),
            'heavy_rain': sum(1 for d in all_data if d['precipitation'] > self.thresholds['heavy_rain']),
            'extreme_rain': sum(1 for d in all_data if d['precipitation'] > self.thresholds['extreme_rain'])
        }
        
        total_records = len(all_data)
        
        print(f"Hot Weather Events (>{self.thresholds['hot_temperature']}°C): {events['hot_days']} ({events['hot_days']/total_records*100:.1f}%)")
        print(f"Cold Weather Events (<{self.thresholds['cold_temperature']}°C): {events['cold_days']} ({events['cold_days']/total_records*100:.1f}%)")
        print(f"High Wind Events (>{self.thresholds['high_wind']} km/h): {events['high_wind']} ({events['high_wind']/total_records*100:.1f}%)")
        print(f"Heavy Rain Events (>{self.thresholds['heavy_rain']} mm): {events['heavy_rain']} ({events['heavy_rain']/total_records*100:.1f}%)")
        print(f"Extreme Rain Events (>{self.thresholds['extreme_rain']} mm): {events['extreme_rain']} ({events['extreme_rain']/total_records*100:.1f}%)")
    
    def show_station_statistics(self):
        """Show detailed statistics for individual stations."""
        print("\n🏢 STATION-SPECIFIC ANALYSIS")
        print("-" * 35)
        
        if not self.stations:
            print("❌ No stations available!")
            return
        
        # List stations
        stations_list = list(self.stations.values())
        print("Available Stations:")
        for i, station in enumerate(stations_list):
            print(f"{i+1}. {station.name} ({station.station_id})")
        
        try:
            choice = int(input(f"\nSelect station (1-{len(stations_list)}): ")) - 1
            
            if 0 <= choice < len(stations_list):
                station = stations_list[choice]
                self.analyze_single_station(station)
            else:
                print("❌ Invalid station selection!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def analyze_single_station(self, station):
        """Perform detailed analysis of a single weather station."""
        print(f"\n📊 ANALYSIS FOR {station.name}")
        print("=" * 50)
        
        if not station.data_points:
            print("❌ No data available for this station!")
            return
        
        print(f"Station ID: {station.station_id}")
        print(f"Location: {station.latitude:.4f}°N, {station.longitude:.4f}°W")
        print(f"Total Measurements: {len(station.data_points):,}")
        print(f"Data Period: {self.get_date_range(station.data_points)}")
        print()
        
        # Calculate statistics for each parameter
        for param in self.weather_types:
            values = [d[param] for d in station.data_points if d[param] is not None]
            
            if not values:
                continue
            
            stats = self.calculate_statistics(values)
            units = self.get_parameter_units(param)
            
            print(f"📈 {param.title().replace('_', ' ')} ({units})")
            print(f"   Average: {stats['mean']:.2f} ± {stats['std_dev']:.2f}")
            print(f"   Range: {stats['min']:.2f} to {stats['max']:.2f}")
            print(f"   Median: {stats['median']:.2f}")
            print(f"   Q1: {stats['q1']:.2f}, Q3: {stats['q3']:.2f}")
            print()
        
        # Show station-specific extreme events
        self.show_station_extreme_events(station)
        
        # Show recent trends
        self.show_recent_trends(station)
    
    def show_station_extreme_events(self, station):
        """Show extreme weather events for a specific station."""
        print("⚠️  EXTREME EVENTS AT THIS STATION")
        print("-" * 40)
        
        extreme_events = []
        
        for measurement in station.data_points:
            events_in_measurement = []
            
            if measurement['temperature'] > self.thresholds['hot_temperature']:
                events_in_measurement.append(f"Hot: {measurement['temperature']:.1f}°C")
            elif measurement['temperature'] < self.thresholds['cold_temperature']:
                events_in_measurement.append(f"Cold: {measurement['temperature']:.1f}°C")
            
            if measurement['wind_speed'] > self.thresholds['high_wind']:
                events_in_measurement.append(f"High Wind: {measurement['wind_speed']:.1f} km/h")
            
            if measurement['precipitation'] > self.thresholds['extreme_rain']:
                events_in_measurement.append(f"Extreme Rain: {measurement['precipitation']:.1f} mm")
            elif measurement['precipitation'] > self.thresholds['heavy_rain']:
                events_in_measurement.append(f"Heavy Rain: {measurement['precipitation']:.1f} mm")
            
            if events_in_measurement:
                extreme_events.append({
                    'timestamp': measurement['timestamp'],
                    'events': events_in_measurement
                })
        
        if extreme_events:
            print(f"Found {len(extreme_events)} extreme weather events:")
            
            # Show most recent 10 events
            recent_events = sorted(extreme_events, key=lambda x: x['timestamp'], reverse=True)[:10]
            
            for event in recent_events:
                print(f"📅 {event['timestamp']}")
                for event_desc in event['events']:
                    print(f"   • {event_desc}")
        else:
            print("✅ No extreme weather events recorded at this station")
    
    def show_recent_trends(self, station):
        """Show recent weather trends for a station."""
        print("\n📈 RECENT TRENDS (Last 7 Days)")
        print("-" * 35)
        
        # Get recent data (last 7 days)
        recent_data = sorted(station.data_points, key=lambda x: x['timestamp'], reverse=True)[:168]  # Assuming 3-hour intervals
        
        if len(recent_data) < 14:  # Need at least some data for trends
            print("❌ Insufficient recent data for trend analysis")
            return
        
        # Split into two periods for comparison
        latest_half = recent_data[:len(recent_data)//2]
        earlier_half = recent_data[len(recent_data)//2:]
        
        for param in ['temperature', 'humidity', 'pressure']:
            latest_values = [d[param] for d in latest_half if d[param] is not None]
            earlier_values = [d[param] for d in earlier_half if d[param] is not None]
            
            if not latest_values or not earlier_values:
                continue
            
            latest_avg = sum(latest_values) / len(latest_values)
            earlier_avg = sum(earlier_values) / len(earlier_values)
            change = latest_avg - earlier_avg
            
            units = self.get_parameter_units(param)
            trend = "↗️" if change > 0 else "↘️" if change < 0 else "➡️"
            
            print(f"{param.title().replace('_', ' ')}: {latest_avg:.1f}{units} {trend} ({change:+.1f})")
    
    def analyze_weather_trends(self):
        """Analyze comprehensive weather trends and patterns."""
        print("\n📈 WEATHER TRENDS & PATTERNS")
        print("-" * 35)
        
        print("Select trend analysis:")
        print("1. Daily Patterns")
        print("2. Weekly Patterns")
        print("3. Seasonal Trends")
        print("4. Long-term Climate Trends")
        print("5. Storm Tracking")
        
        try:
            choice = int(input("Enter choice (1-5): "))
            
            if choice == 1:
                self.analyze_daily_patterns()
            elif choice == 2:
                self.analyze_weekly_patterns()
            elif choice == 3:
                self.analyze_seasonal_trends()
            elif choice == 4:
                self.analyze_climate_trends()
            elif choice == 5:
                self.track_storm_systems()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def analyze_daily_patterns(self):
        """Analyze daily weather patterns across all stations."""
        print("\n🌅 DAILY WEATHER PATTERNS")
        print("-" * 30)
        
        # Collect hourly data
        hourly_data = {}
        for hour in range(24):
            hourly_data[hour] = {'temperature': [], 'humidity': [], 'wind_speed': []}
        
        # Process all data points
        for station in self.stations.values():
            for measurement in station.data_points:
                try:
                    # Extract hour from timestamp (assuming format: "YYYY-MM-DD HH:MM:SS")
                    hour = int(measurement['timestamp'].split()[1].split(':')[0])
                    
                    hourly_data[hour]['temperature'].append(measurement['temperature'])
                    hourly_data[hour]['humidity'].append(measurement['humidity'])
                    hourly_data[hour]['wind_speed'].append(measurement['wind_speed'])
                except (ValueError, IndexError):
                    continue
        
        # Calculate averages and display patterns
        print("Hour | Temperature | Humidity | Wind Speed")
        print("-" * 45)
        
        for hour in range(24):
            temp_avg = sum(hourly_data[hour]['temperature']) / len(hourly_data[hour]['temperature']) if hourly_data[hour]['temperature'] else 0
            humid_avg = sum(hourly_data[hour]['humidity']) / len(hourly_data[hour]['humidity']) if hourly_data[hour]['humidity'] else 0
            wind_avg = sum(hourly_data[hour]['wind_speed']) / len(hourly_data[hour]['wind_speed']) if hourly_data[hour]['wind_speed'] else 0
            
            print(f"{hour:2d}:00 | {temp_avg:8.1f}°C | {humid_avg:6.1f}%  | {wind_avg:7.1f} km/h")
        
        # Identify patterns
        temps = [sum(hourly_data[h]['temperature']) / len(hourly_data[h]['temperature']) 
                if hourly_data[h]['temperature'] else 0 for h in range(24)]
        
        max_temp_hour = temps.index(max(temps))
        min_temp_hour = temps.index(min(temps))
        
        print(f"\n🌡️  Temperature Patterns:")
        print(f"   Warmest hour: {max_temp_hour:2d}:00 ({max(temps):.1f}°C)")
        print(f"   Coolest hour: {min_temp_hour:2d}:00 ({min(temps):.1f}°C)")
        print(f"   Daily range: {max(temps) - min(temps):.1f}°C")
    
    def create_text_chart(self, data, title, width=50):
        """Create a simple text-based chart for data visualization."""
        print(f"\n📊 {title}")
        print("-" * len(title))
        
        if not data:
            print("No data to display")
            return
        
        min_val = min(data)
        max_val = max(data)
        range_val = max_val - min_val
        
        if range_val == 0:
            print("All values are the same")
            return
        
        for i, value in enumerate(data):
            # Normalize value to chart width
            bar_length = int(((value - min_val) / range_val) * width)
            bar = "█" * bar_length + "░" * (width - bar_length)
            print(f"{i:2d}: {bar} {value:.1f}")
    
    def run(self):
        """Main program loop."""
        print("🌤️ Welcome to the Weather Analysis System!")
        print("Monitor, analyze, and understand weather patterns with comprehensive data tools.")
        
        while True:
            self.display_main_menu()
            choice = self.get_menu_choice()
            
            if choice == 0:
                print("\n🌤️ Thank you for using the Weather Analysis System!")
                print("Stay informed and stay safe!")
                break
            elif choice == 1:
                self.display_station_information()
            elif choice == 2:
                self.show_current_conditions()
            elif choice == 3:
                self.perform_statistical_analysis()
            elif choice == 4:
                self.analyze_weather_trends()
            elif choice == 5:
                print("🚧 Extreme weather detection feature coming soon!")
            elif choice == 6:
                print("🚧 Comparative analysis feature coming soon!")
            elif choice == 7:
                print("🚧 Weather reports feature coming soon!")
            elif choice == 8:
                print("🚧 Data visualization feature coming soon!")
            elif choice == 9:
                print("🚧 Weather prediction feature coming soon!")
            elif choice == 10:
                print("🚧 System administration feature coming soon!")
            
            print("\n" + "=" * 60)
            input("Press Enter to continue...")

def main():
    """Main entry point for the program."""
    weather_system = WeatherAnalysisSystem()
    weather_system.run()

if __name__ == "__main__":
    main()

"""
SOLUTION REQUIREMENTS:
=====================
Your solution should include:
1. ✅ Multi-dimensional weather data storage and management
2. ✅ Comprehensive statistical analysis capabilities
3. ✅ Pattern recognition and trend analysis
4. ✅ Data visualization through text-based charts
5. ✅ Extreme weather event detection and reporting
6. ✅ Professional user interface with clear navigation
7. ✅ Realistic weather data simulation and processing
8. ✅ Scientific accuracy in calculations and analysis

LEARNING OUTCOMES:
==================
After completing this problem, you will have mastered:
• Multi-dimensional array processing and data structures
• Statistical analysis and mathematical computations
• Time series data analysis and pattern recognition
• Scientific computing principles and methodologies
• Data visualization techniques and presentation
• Professional system design and user experience
• Weather science and meteorological concepts
• Large-scale data processing and optimization

EXTENSION IDEAS:
===============
1. Add real weather API integration for live data
2. Implement advanced forecasting algorithms
3. Create graphical charts using plotting libraries
4. Add weather alerts and notification system
5. Implement data export to CSV/JSON formats
6. Add machine learning for pattern prediction
7. Create weather maps and geographical analysis
8. Add climate change analysis and reporting

This problem provides comprehensive practice with arrays, statistics,
data analysis, and scientific computing while creating a genuinely
useful meteorological analysis tool!
"""