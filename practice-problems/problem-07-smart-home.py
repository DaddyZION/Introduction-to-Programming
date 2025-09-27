"""
Practice Problem 07: Smart Home Automation System
===============================================

DIFFICULTY: Expert ⭐⭐⭐⭐
CONCEPTS: Advanced Integration of All Course Concepts
ASSIGNMENTS: Comprehensive integration of assignments 1-7
ESTIMATED TIME: 120-150 minutes

PROBLEM DESCRIPTION:
===================
Create a comprehensive smart home automation system that manages multiple IoT devices,
monitors environmental conditions, controls home security, manages energy consumption,
and provides intelligent automation based on user preferences and learned patterns.

This expert-level problem integrates all programming concepts from the course including
sequences, selection, iteration, validation, functions, arrays/strings, and 2D arrays
to create a sophisticated home automation platform.

REQUIREMENTS:
============
1. Device management (lights, thermostats, security cameras, sensors)
2. Environmental monitoring and climate control
3. Security system with alerts and monitoring
4. Energy consumption tracking and optimization
5. Automated scheduling and rule-based control
6. User preference learning and adaptive behavior
7. Emergency detection and response protocols
8. Integration with external services and notifications

LEARNING OBJECTIVES:
===================
- Master integration of all programming fundamentals
- Understand IoT and automation system design
- Practice complex decision-making algorithms
- Implement machine learning-like pattern recognition
- Design enterprise-level software architecture
- Work with real-time data processing and control systems

STARTER CODE:
============
"""

import random
import math
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional, Any
from enum import Enum
from abc import ABC, abstractmethod

class DeviceType(Enum):
    LIGHT = "light"
    THERMOSTAT = "thermostat"
    SECURITY_CAMERA = "security_camera" 
    DOOR_LOCK = "door_lock"
    SENSOR = "sensor"
    APPLIANCE = "appliance"

class DeviceStatus(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    MAINTENANCE = "maintenance"
    ERROR = "error"

class SecurityLevel(Enum):
    DISARMED = "disarmed"
    HOME = "home"
    AWAY = "away"
    VACATION = "vacation"

class SmartDevice(ABC):
    """Abstract base class for all smart home devices."""
    
    def __init__(self, device_id: str, name: str, location: str, device_type: DeviceType):
        self.device_id = device_id
        self.name = name
        self.location = location
        self.device_type = device_type
        self.status = DeviceStatus.ONLINE
        self.last_updated = datetime.now()
        self.energy_consumption = 0.0  # Watts
        self.settings = {}
        self.activity_log = []
    
    @abstractmethod
    def update_state(self, new_state: Dict[str, Any]) -> bool:
        """Update device state with new values."""
        pass
    
    @abstractmethod
    def get_current_state(self) -> Dict[str, Any]:
        """Get current device state."""
        pass
    
    def log_activity(self, activity: str):
        """Log device activity with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activity_log.append({
            'timestamp': timestamp,
            'activity': activity,
            'device_id': self.device_id
        })
        
        # Keep only last 100 activities
        if len(self.activity_log) > 100:
            self.activity_log = self.activity_log[-100:]

class SmartLight(SmartDevice):
    """Smart light with dimming and color control."""
    
    def __init__(self, device_id: str, name: str, location: str):
        super().__init__(device_id, name, location, DeviceType.LIGHT)
        self.is_on = False
        self.brightness = 100  # 0-100%
        self.color_temp = 3000  # Kelvin (2700-6500)
        self.rgb_color = (255, 255, 255)  # RGB values
        self.energy_consumption = 0.0  # Varies by brightness
    
    def update_state(self, new_state: Dict[str, Any]) -> bool:
        """Update light state."""
        try:
            if 'power' in new_state:
                self.is_on = new_state['power']
                self.log_activity(f"Power {'ON' if self.is_on else 'OFF'}")
            
            if 'brightness' in new_state:
                self.brightness = max(0, min(100, new_state['brightness']))
                self.log_activity(f"Brightness set to {self.brightness}%")
            
            if 'color_temp' in new_state:
                self.color_temp = max(2700, min(6500, new_state['color_temp']))
                self.log_activity(f"Color temperature set to {self.color_temp}K")
            
            # Update energy consumption
            if self.is_on:
                self.energy_consumption = (self.brightness / 100) * 12  # 12W max
            else:
                self.energy_consumption = 0.1  # Standby power
            
            self.last_updated = datetime.now()
            return True
        
        except Exception as e:
            self.log_activity(f"Error updating state: {e}")
            return False
    
    def get_current_state(self) -> Dict[str, Any]:
        """Get current light state."""
        return {
            'device_id': self.device_id,
            'name': self.name,
            'location': self.location,
            'type': self.device_type.value,
            'power': self.is_on,
            'brightness': self.brightness,
            'color_temp': self.color_temp,
            'rgb_color': self.rgb_color,
            'energy_consumption': self.energy_consumption,
            'status': self.status.value,
            'last_updated': self.last_updated.strftime("%Y-%m-%d %H:%M:%S")
        }

class SmartThermostat(SmartDevice):
    """Smart thermostat with learning capabilities."""
    
    def __init__(self, device_id: str, name: str, location: str):
        super().__init__(device_id, name, location, DeviceType.THERMOSTAT)
        self.current_temp = 22.0  # Celsius
        self.target_temp = 22.0
        self.mode = "auto"  # auto, heat, cool, off
        self.humidity = 45.0  # Percentage
        self.is_heating = False
        self.is_cooling = False
        self.schedule = {}  # Time-based temperature settings
        self.learning_data = []  # User preference learning
        self.energy_consumption = 0.0
    
    def update_state(self, new_state: Dict[str, Any]) -> bool:
        """Update thermostat state."""
        try:
            if 'target_temp' in new_state:
                old_target = self.target_temp
                self.target_temp = max(15, min(30, new_state['target_temp']))
                self.log_activity(f"Target temperature changed from {old_target}°C to {self.target_temp}°C")
                
                # Record for learning
                self.learning_data.append({
                    'timestamp': datetime.now(),
                    'temperature_change': self.target_temp - old_target,
                    'current_temp': self.current_temp,
                    'time_of_day': datetime.now().hour,
                    'day_of_week': datetime.now().weekday()
                })
            
            if 'mode' in new_state:
                self.mode = new_state['mode']
                self.log_activity(f"Mode set to {self.mode}")
            
            # Simulate HVAC operation
            self.simulate_hvac_operation()
            self.last_updated = datetime.now()
            return True
        
        except Exception as e:
            self.log_activity(f"Error updating state: {e}")
            return False
    
    def simulate_hvac_operation(self):
        """Simulate heating/cooling system operation."""
        temp_diff = abs(self.current_temp - self.target_temp)
        
        if self.mode == "auto" or self.mode == "heat":
            if self.current_temp < self.target_temp - 0.5:
                self.is_heating = True
                self.is_cooling = False
                self.energy_consumption = 2500.0  # 2.5kW heating
            elif self.current_temp > self.target_temp + 0.5:
                if self.mode == "auto":
                    self.is_cooling = True
                    self.is_heating = False
                    self.energy_consumption = 1800.0  # 1.8kW cooling
            else:
                self.is_heating = False
                self.is_cooling = False
                self.energy_consumption = 25.0  # Standby power
        
        # Simulate temperature change
        if self.is_heating:
            self.current_temp += random.uniform(0.1, 0.3)
        elif self.is_cooling:
            self.current_temp -= random.uniform(0.1, 0.3)
        else:
            # Natural temperature drift
            self.current_temp += random.uniform(-0.1, 0.1)
    
    def get_current_state(self) -> Dict[str, Any]:
        """Get current thermostat state."""
        return {
            'device_id': self.device_id,
            'name': self.name,
            'location': self.location,
            'type': self.device_type.value,
            'current_temp': round(self.current_temp, 1),
            'target_temp': self.target_temp,
            'mode': self.mode,
            'humidity': round(self.humidity, 1),
            'is_heating': self.is_heating,
            'is_cooling': self.is_cooling,
            'energy_consumption': self.energy_consumption,
            'status': self.status.value,
            'last_updated': self.last_updated.strftime("%Y-%m-%d %H:%M:%S")
        }

class SecurityCamera(SmartDevice):
    """Security camera with motion detection."""
    
    def __init__(self, device_id: str, name: str, location: str):
        super().__init__(device_id, name, location, DeviceType.SECURITY_CAMERA)
        self.is_recording = False
        self.motion_detected = False
        self.last_motion_time = None
        self.recording_quality = "1080p"
        self.night_vision = True
        self.motion_sensitivity = 50  # 0-100
        self.recorded_events = []
        self.energy_consumption = 8.0  # Constant power draw
    
    def update_state(self, new_state: Dict[str, Any]) -> bool:
        """Update camera state."""
        try:
            if 'recording' in new_state:
                self.is_recording = new_state['recording']
                self.log_activity(f"Recording {'started' if self.is_recording else 'stopped'}")
            
            if 'motion_sensitivity' in new_state:
                self.motion_sensitivity = max(0, min(100, new_state['motion_sensitivity']))
                self.log_activity(f"Motion sensitivity set to {self.motion_sensitivity}")
            
            # Simulate motion detection
            if random.random() < 0.05:  # 5% chance of motion each update
                self.detect_motion()
            
            self.last_updated = datetime.now()
            return True
        
        except Exception as e:
            self.log_activity(f"Error updating state: {e}")
            return False
    
    def detect_motion(self):
        """Simulate motion detection."""
        self.motion_detected = True
        self.last_motion_time = datetime.now()
        
        # Start recording if not already recording
        if not self.is_recording:
            self.is_recording = True
        
        # Log motion event
        event = {
            'timestamp': self.last_motion_time.strftime("%Y-%m-%d %H:%M:%S"),
            'type': 'motion_detected',
            'location': self.location,
            'confidence': random.randint(60, 95)
        }
        
        self.recorded_events.append(event)
        self.log_activity(f"Motion detected in {self.location}")
        
        # Keep only last 50 events
        if len(self.recorded_events) > 50:
            self.recorded_events = self.recorded_events[-50:]
    
    def get_current_state(self) -> Dict[str, Any]:
        """Get current camera state."""
        return {
            'device_id': self.device_id,
            'name': self.name,
            'location': self.location,
            'type': self.device_type.value,
            'recording': self.is_recording,
            'motion_detected': self.motion_detected,
            'last_motion_time': self.last_motion_time.strftime("%Y-%m-%d %H:%M:%S") if self.last_motion_time else None,
            'quality': self.recording_quality,
            'night_vision': self.night_vision,
            'motion_sensitivity': self.motion_sensitivity,
            'energy_consumption': self.energy_consumption,
            'status': self.status.value,
            'last_updated': self.last_updated.strftime("%Y-%m-%d %H:%M:%S")
        }

class EnvironmentSensor(SmartDevice):
    """Environmental sensor for temperature, humidity, air quality."""
    
    def __init__(self, device_id: str, name: str, location: str):
        super().__init__(device_id, name, location, DeviceType.SENSOR)
        self.temperature = 22.0
        self.humidity = 45.0
        self.air_quality = 85  # 0-100 (higher is better)
        self.light_level = 300  # Lux
        self.noise_level = 35  # Decibels
        self.readings_history = []
        self.energy_consumption = 2.0  # Low power sensor
    
    def update_state(self, new_state: Dict[str, Any]) -> bool:
        """Update sensor readings (simulated)."""
        try:
            # Simulate realistic environmental changes
            self.temperature += random.uniform(-0.2, 0.2)
            self.humidity += random.uniform(-1.0, 1.0)
            self.air_quality += random.uniform(-2, 2)
            self.light_level = max(0, self.light_level + random.uniform(-20, 20))
            self.noise_level = max(20, min(80, self.noise_level + random.uniform(-5, 5)))
            
            # Keep readings within realistic ranges
            self.temperature = max(15, min(35, self.temperature))
            self.humidity = max(20, min(80, self.humidity))
            self.air_quality = max(0, min(100, self.air_quality))
            
            # Store reading in history
            reading = {
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'temperature': round(self.temperature, 1),
                'humidity': round(self.humidity, 1),
                'air_quality': round(self.air_quality),
                'light_level': round(self.light_level),
                'noise_level': round(self.noise_level, 1)
            }
            
            self.readings_history.append(reading)
            
            # Keep only last 288 readings (24 hours at 5-minute intervals)
            if len(self.readings_history) > 288:
                self.readings_history = self.readings_history[-288:]
            
            # Check for alerts
            self.check_environmental_alerts()
            
            self.last_updated = datetime.now()
            return True
        
        except Exception as e:
            self.log_activity(f"Error updating readings: {e}")
            return False
    
    def check_environmental_alerts(self):
        """Check for environmental conditions requiring alerts."""
        alerts = []
        
        if self.temperature > 28:
            alerts.append("High temperature detected")
        elif self.temperature < 18:
            alerts.append("Low temperature detected")
        
        if self.humidity > 70:
            alerts.append("High humidity detected")
        elif self.humidity < 30:
            alerts.append("Low humidity detected")
        
        if self.air_quality < 50:
            alerts.append("Poor air quality detected")
        
        if self.noise_level > 60:
            alerts.append("High noise level detected")
        
        for alert in alerts:
            self.log_activity(f"ALERT: {alert}")
    
    def get_current_state(self) -> Dict[str, Any]:
        """Get current sensor state."""
        return {
            'device_id': self.device_id,
            'name': self.name,
            'location': self.location,
            'type': self.device_type.value,
            'temperature': round(self.temperature, 1),
            'humidity': round(self.humidity, 1),
            'air_quality': round(self.air_quality),
            'light_level': round(self.light_level),
            'noise_level': round(self.noise_level, 1),
            'energy_consumption': self.energy_consumption,
            'status': self.status.value,
            'last_updated': self.last_updated.strftime("%Y-%m-%d %H:%M:%S")
        }

class SmartHomeSystem:
    """Main smart home automation system controller."""
    
    def __init__(self):
        """Initialize the smart home system."""
        self.devices = {}  # device_id -> SmartDevice
        self.automation_rules = {}  # rule_id -> automation_rule
        self.user_preferences = {}
        self.security_level = SecurityLevel.DISARMED
        self.system_alerts = []
        self.energy_usage_history = []
        self.occupancy_status = "unknown"  # home, away, sleeping
        self.learning_engine = LearningEngine()
        
        # System statistics
        self.total_devices = 0
        self.online_devices = 0
        self.total_energy_consumption = 0.0
        
        # Initialize with sample devices
        self.initialize_sample_devices()
        
        # Initialize automation rules
        self.initialize_automation_rules()
    
    def initialize_sample_devices(self):
        """Initialize system with sample smart devices."""
        # Sample lights
        lights = [
            ("L001", "Living Room Main Light", "living_room"),
            ("L002", "Kitchen Pendant Lights", "kitchen"),
            ("L003", "Master Bedroom Light", "master_bedroom"),
            ("L004", "Guest Bedroom Light", "guest_bedroom"),
            ("L005", "Bathroom Vanity Light", "bathroom"),
            ("L006", "Outdoor Porch Light", "outdoor")
        ]
        
        for device_id, name, location in lights:
            light = SmartLight(device_id, name, location)
            # Randomize initial state
            light.update_state({
                'power': random.choice([True, False]),
                'brightness': random.randint(20, 100),
                'color_temp': random.randint(2700, 6500)
            })
            self.devices[device_id] = light
        
        # Sample thermostats
        thermostats = [
            ("T001", "Main Thermostat", "living_room"),
            ("T002", "Bedroom Thermostat", "master_bedroom")
        ]
        
        for device_id, name, location in thermostats:
            thermostat = SmartThermostat(device_id, name, location)
            thermostat.update_state({
                'target_temp': random.uniform(20, 25),
                'mode': random.choice(['auto', 'heat', 'cool'])
            })
            self.devices[device_id] = thermostat
        
        # Sample security cameras
        cameras = [
            ("C001", "Front Door Camera", "front_door"),
            ("C002", "Backyard Camera", "backyard"),
            ("C003", "Garage Camera", "garage"),
            ("C004", "Living Room Camera", "living_room")
        ]
        
        for device_id, name, location in cameras:
            camera = SecurityCamera(device_id, name, location)
            camera.update_state({
                'recording': random.choice([True, False]),
                'motion_sensitivity': random.randint(30, 80)
            })
            self.devices[device_id] = camera
        
        # Sample environmental sensors
        sensors = [
            ("S001", "Living Room Sensor", "living_room"),
            ("S002", "Kitchen Sensor", "kitchen"),
            ("S003", "Master Bedroom Sensor", "master_bedroom"),
            ("S004", "Outdoor Sensor", "outdoor")
        ]
        
        for device_id, name, location in sensors:
            sensor = EnvironmentSensor(device_id, name, location)
            sensor.update_state({})  # Initialize with random readings
            self.devices[device_id] = sensor
        
        self.update_system_statistics()
    
    def initialize_automation_rules(self):
        """Initialize default automation rules."""
        self.automation_rules = {
            "evening_lights": {
                "name": "Evening Light Schedule",
                "trigger": "time_based",
                "conditions": {"time": "18:00", "occupancy": "home"},
                "actions": [
                    {"device_type": "light", "location": "living_room", "power": True, "brightness": 80},
                    {"device_type": "light", "location": "kitchen", "power": True, "brightness": 60}
                ],
                "enabled": True
            },
            "security_away": {
                "name": "Away Mode Security",
                "trigger": "occupancy_change",
                "conditions": {"occupancy": "away"},
                "actions": [
                    {"device_type": "security_camera", "recording": True},
                    {"device_type": "light", "power": False}
                ],
                "enabled": True
            },
            "energy_saver": {
                "name": "Night Energy Saver",
                "trigger": "time_based",
                "conditions": {"time": "23:00", "occupancy": "sleeping"},
                "actions": [
                    {"device_type": "thermostat", "target_temp": 20},
                    {"device_type": "light", "power": False}
                ],
                "enabled": True
            },
            "morning_routine": {
                "name": "Morning Activation",
                "trigger": "time_based",
                "conditions": {"time": "07:00", "day_of_week": "weekday"},
                "actions": [
                    {"device_type": "thermostat", "target_temp": 22},
                    {"device_type": "light", "location": "kitchen", "power": True, "brightness": 100}
                ],
                "enabled": True
            }
        }
    
    def display_main_menu(self):
        """Display the main menu options."""
        print("=" * 70)
        print("              SMART HOME AUTOMATION SYSTEM")
        print("=" * 70)
        print("1. Device Management & Control")
        print("2. Environmental Monitoring")
        print("3. Security System Management")
        print("4. Energy Management & Analytics")
        print("5. Automation Rules & Scheduling")
        print("6. System Analytics & Reports")
        print("7. User Preferences & Learning")
        print("8. Emergency Systems & Alerts")
        print("9. System Diagnostics & Maintenance")
        print("10. Integration & External Services")
        print("0. Exit")
        print("=" * 70)
    
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
    
    def device_management(self):
        """Device management and control interface."""
        print("\n🏠 DEVICE MANAGEMENT & CONTROL")
        print("-" * 40)
        
        print("1. View All Devices")
        print("2. Control Individual Device")
        print("3. Room-based Control")
        print("4. Device Status & Health")
        print("5. Add New Device")
        print("6. Remove Device")
        print("7. Device Groups Management")
        
        try:
            choice = int(input("Enter choice (1-7): "))
            
            if choice == 1:
                self.view_all_devices()
            elif choice == 2:
                self.control_individual_device()
            elif choice == 3:
                self.room_based_control()
            elif choice == 4:
                self.device_status_health()
            elif choice == 5:
                print("🚧 Add device feature coming soon!")
            elif choice == 6:
                print("🚧 Remove device feature coming soon!")
            elif choice == 7:
                print("🚧 Device groups feature coming soon!")
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def view_all_devices(self):
        """Display overview of all smart devices."""
        print("\n📱 ALL SMART DEVICES")
        print("-" * 30)
        
        if not self.devices:
            print("❌ No devices found!")
            return
        
        self.update_system_statistics()
        
        print(f"Total Devices: {self.total_devices}")
        print(f"Online Devices: {self.online_devices}")
        print(f"Total Power Consumption: {self.total_energy_consumption:.1f} W")
        print()
        
        # Group devices by type
        device_groups = {}
        for device in self.devices.values():
            device_type = device.device_type.value
            if device_type not in device_groups:
                device_groups[device_type] = []
            device_groups[device_type].append(device)
        
        # Display each group
        for device_type, devices in device_groups.items():
            print(f"📌 {device_type.upper().replace('_', ' ')} ({len(devices)} devices)")
            print("-" * 50)
            
            for device in devices:
                status_emoji = {"online": "🟢", "offline": "🔴", "maintenance": "🟡", "error": "❌"}
                emoji = status_emoji.get(device.status.value, "⚪")
                
                state = device.get_current_state()
                
                if device_type == "light":
                    power_status = "ON" if state['power'] else "OFF"
                    print(f"  {emoji} {device.name} ({device.location}): {power_status}")
                    if state['power']:
                        print(f"      Brightness: {state['brightness']}%, Power: {state['energy_consumption']:.1f}W")
                
                elif device_type == "thermostat":
                    print(f"  {emoji} {device.name} ({device.location}): {state['current_temp']}°C → {state['target_temp']}°C")
                    print(f"      Mode: {state['mode']}, Power: {state['energy_consumption']:.0f}W")
                
                elif device_type == "security_camera":
                    rec_status = "Recording" if state['recording'] else "Standby"
                    print(f"  {emoji} {device.name} ({device.location}): {rec_status}")
                    if state['last_motion_time']:
                        print(f"      Last Motion: {state['last_motion_time']}")
                
                elif device_type == "sensor":
                    print(f"  {emoji} {device.name} ({device.location}): T:{state['temperature']}°C H:{state['humidity']}%")
                    print(f"      Air Quality: {state['air_quality']}/100, Light: {state['light_level']} lux")
            
            print()
    
    def control_individual_device(self):
        """Control individual smart device."""
        print("\n🎮 INDIVIDUAL DEVICE CONTROL")
        print("-" * 35)
        
        if not self.devices:
            print("❌ No devices available!")
            return
        
        # List devices for selection
        devices_list = list(self.devices.values())
        print("Select a device to control:")
        
        for i, device in enumerate(devices_list, 1):
            status_emoji = {"online": "🟢", "offline": "🔴", "maintenance": "🟡", "error": "❌"}
            emoji = status_emoji.get(device.status.value, "⚪")
            print(f"{i:2d}. {emoji} {device.name} ({device.location}) - {device.device_type.value}")
        
        try:
            choice = int(input(f"Enter choice (1-{len(devices_list)}): ")) - 1
            
            if 0 <= choice < len(devices_list):
                device = devices_list[choice]
                self.control_specific_device(device)
            else:
                print("❌ Invalid selection!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def control_specific_device(self, device: SmartDevice):
        """Control a specific device based on its type."""
        print(f"\n🎛️ CONTROLLING: {device.name}")
        print("-" * 40)
        
        current_state = device.get_current_state()
        
        if device.device_type == DeviceType.LIGHT:
            self.control_light(device, current_state)
        elif device.device_type == DeviceType.THERMOSTAT:
            self.control_thermostat(device, current_state)
        elif device.device_type == DeviceType.SECURITY_CAMERA:
            self.control_camera(device, current_state)
        else:
            print("❌ Device type not supported for direct control")
    
    def control_light(self, light: SmartLight, current_state: Dict[str, Any]):
        """Control smart light settings."""
        print(f"Current Status: {'ON' if current_state['power'] else 'OFF'}")
        print(f"Brightness: {current_state['brightness']}%")
        print(f"Color Temperature: {current_state['color_temp']}K")
        print()
        
        print("Available controls:")
        print("1. Toggle Power")
        print("2. Set Brightness")
        print("3. Set Color Temperature")
        print("4. Set Scene (Warm/Cool/Bright)")
        
        try:
            choice = int(input("Enter choice (1-4): "))
            new_state = {}
            
            if choice == 1:
                new_state['power'] = not current_state['power']
                print(f"Light {'turned ON' if new_state['power'] else 'turned OFF'}")
            
            elif choice == 2:
                brightness = int(input("Enter brightness (0-100): "))
                if 0 <= brightness <= 100:
                    new_state['brightness'] = brightness
                    print(f"Brightness set to {brightness}%")
                else:
                    print("❌ Brightness must be between 0-100")
                    return
            
            elif choice == 3:
                color_temp = int(input("Enter color temperature (2700-6500K): "))
                if 2700 <= color_temp <= 6500:
                    new_state['color_temp'] = color_temp
                    print(f"Color temperature set to {color_temp}K")
                else:
                    print("❌ Color temperature must be between 2700-6500K")
                    return
            
            elif choice == 4:
                print("Scene options:")
                print("1. Warm (2700K, 60%)")
                print("2. Cool (5000K, 80%)")
                print("3. Bright (4000K, 100%)")
                
                scene = int(input("Select scene (1-3): "))
                if scene == 1:
                    new_state.update({'power': True, 'brightness': 60, 'color_temp': 2700})
                elif scene == 2:
                    new_state.update({'power': True, 'brightness': 80, 'color_temp': 5000})
                elif scene == 3:
                    new_state.update({'power': True, 'brightness': 100, 'color_temp': 4000})
                else:
                    print("❌ Invalid scene selection")
                    return
                
                print("Scene applied successfully!")
            
            else:
                print("❌ Invalid choice!")
                return
            
            # Apply the changes
            if new_state and light.update_state(new_state):
                print("✅ Device updated successfully!")
            else:
                print("❌ Failed to update device!")
        
        except ValueError:
            print("❌ Please enter valid numbers!")
    
    def control_thermostat(self, thermostat: SmartThermostat, current_state: Dict[str, Any]):
        """Control smart thermostat settings."""
        print(f"Current Temperature: {current_state['current_temp']}°C")
        print(f"Target Temperature: {current_state['target_temp']}°C")
        print(f"Mode: {current_state['mode']}")
        print(f"Status: {'Heating' if current_state['is_heating'] else 'Cooling' if current_state['is_cooling'] else 'Idle'}")
        print()
        
        print("Available controls:")
        print("1. Set Target Temperature")
        print("2. Change Mode")
        print("3. Quick Adjustments (+/- 1°C)")
        
        try:
            choice = int(input("Enter choice (1-3): "))
            new_state = {}
            
            if choice == 1:
                temp = float(input("Enter target temperature (15-30°C): "))
                if 15 <= temp <= 30:
                    new_state['target_temp'] = temp
                    print(f"Target temperature set to {temp}°C")
                else:
                    print("❌ Temperature must be between 15-30°C")
                    return
            
            elif choice == 2:
                print("Mode options:")
                print("1. Auto")
                print("2. Heat")
                print("3. Cool")
                print("4. Off")
                
                mode_choice = int(input("Select mode (1-4): "))
                modes = ["", "auto", "heat", "cool", "off"]
                
                if 1 <= mode_choice <= 4:
                    new_state['mode'] = modes[mode_choice]
                    print(f"Mode set to {modes[mode_choice]}")
                else:
                    print("❌ Invalid mode selection")
                    return
            
            elif choice == 3:
                print("1. Increase by 1°C")
                print("2. Decrease by 1°C")
                
                adj_choice = int(input("Select adjustment (1-2): "))
                current_target = current_state['target_temp']
                
                if adj_choice == 1:
                    new_temp = min(30, current_target + 1)
                    new_state['target_temp'] = new_temp
                    print(f"Temperature increased to {new_temp}°C")
                elif adj_choice == 2:
                    new_temp = max(15, current_target - 1)
                    new_state['target_temp'] = new_temp
                    print(f"Temperature decreased to {new_temp}°C")
                else:
                    print("❌ Invalid adjustment selection")
                    return
            
            else:
                print("❌ Invalid choice!")
                return
            
            # Apply the changes
            if new_state and thermostat.update_state(new_state):
                print("✅ Thermostat updated successfully!")
            else:
                print("❌ Failed to update thermostat!")
        
        except ValueError:
            print("❌ Please enter valid numbers!")
    
    def update_system_statistics(self):
        """Update overall system statistics."""
        self.total_devices = len(self.devices)
        self.online_devices = sum(1 for device in self.devices.values() 
                                 if device.status == DeviceStatus.ONLINE)
        self.total_energy_consumption = sum(device.energy_consumption 
                                          for device in self.devices.values())
    
    def environmental_monitoring(self):
        """Environmental monitoring and climate control."""
        print("\n🌡️ ENVIRONMENTAL MONITORING")
        print("-" * 35)
        
        print("1. Current Environmental Status")
        print("2. Environmental History & Trends")
        print("3. Climate Control Settings")
        print("4. Air Quality Management")
        print("5. Environmental Alerts & Thresholds")
        
        try:
            choice = int(input("Enter choice (1-5): "))
            
            if choice == 1:
                self.show_current_environmental_status()
            elif choice == 2:
                self.show_environmental_history()
            elif choice == 3:
                print("🚧 Climate control settings coming soon!")
            elif choice == 4:
                print("🚧 Air quality management coming soon!")
            elif choice == 5:
                print("🚧 Environmental alerts coming soon!")
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def show_current_environmental_status(self):
        """Display current environmental conditions from all sensors."""
        print("\n🌡️ CURRENT ENVIRONMENTAL STATUS")
        print("-" * 40)
        
        # Get all environmental sensors
        sensors = [device for device in self.devices.values() 
                  if device.device_type == DeviceType.SENSOR]
        
        if not sensors:
            print("❌ No environmental sensors found!")
            return
        
        print(f"{'Location':<15} {'Temp':<8} {'Humidity':<8} {'Air Quality':<12} {'Light':<10} {'Noise'}")
        print("-" * 70)
        
        total_temp = 0
        total_humidity = 0
        total_air_quality = 0
        
        for sensor in sensors:
            state = sensor.get_current_state()
            
            temp_status = "🔥" if state['temperature'] > 25 else "❄️" if state['temperature'] < 18 else "🌡️"
            humid_status = "💧" if state['humidity'] > 60 else "🏜️" if state['humidity'] < 30 else "💨"
            air_status = "✅" if state['air_quality'] > 70 else "⚠️" if state['air_quality'] > 50 else "🚫"
            
            print(f"{state['location']:<15} {temp_status}{state['temperature']:>4.1f}°C "
                  f"{humid_status}{state['humidity']:>4.0f}% {air_status}{state['air_quality']:>8}/100 "
                  f"{state['light_level']:>6} lux {state['noise_level']:>4.0f} dB")
            
            total_temp += state['temperature']
            total_humidity += state['humidity']
            total_air_quality += state['air_quality']
        
        # Calculate averages
        num_sensors = len(sensors)
        avg_temp = total_temp / num_sensors
        avg_humidity = total_humidity / num_sensors
        avg_air_quality = total_air_quality / num_sensors
        
        print("-" * 70)
        print(f"{'AVERAGE':<15} {avg_temp:>6.1f}°C {avg_humidity:>6.0f}% "
              f"{avg_air_quality:>12.0f}/100")
        
        # Overall comfort assessment
        print(f"\n🏠 OVERALL COMFORT ASSESSMENT")
        print("-" * 35)
        
        comfort_score = 0
        max_score = 0
        
        # Temperature comfort (ideal: 20-24°C)
        if 20 <= avg_temp <= 24:
            temp_comfort = 100
        elif 18 <= avg_temp <= 26:
            temp_comfort = 80
        else:
            temp_comfort = 40
        
        comfort_score += temp_comfort
        max_score += 100
        
        # Humidity comfort (ideal: 40-60%)
        if 40 <= avg_humidity <= 60:
            humidity_comfort = 100
        elif 30 <= avg_humidity <= 70:
            humidity_comfort = 80
        else:
            humidity_comfort = 40
        
        comfort_score += humidity_comfort
        max_score += 100
        
        # Air quality comfort
        air_comfort = avg_air_quality
        comfort_score += air_comfort
        max_score += 100
        
        overall_comfort = (comfort_score / max_score) * 100
        
        comfort_emoji = "😊" if overall_comfort >= 80 else "😐" if overall_comfort >= 60 else "😟"
        
        print(f"Temperature Comfort: {temp_comfort}%")
        print(f"Humidity Comfort: {humidity_comfort}%")
        print(f"Air Quality: {air_comfort:.0f}%")
        print(f"Overall Comfort: {comfort_emoji} {overall_comfort:.0f}%")
    
    def run(self):
        """Main program loop."""
        print("🏠 Welcome to the Smart Home Automation System!")
        print("Intelligent control and monitoring for your connected home.")
        
        # Simulate system startup
        print("\n🔄 Initializing smart home systems...")
        print("   ✅ Device discovery complete")
        print("   ✅ Automation rules loaded")
        print("   ✅ Security systems online")
        print("   ✅ Environmental monitoring active")
        
        while True:
            # Simulate device updates
            for device in list(self.devices.values())[:3]:  # Update first 3 devices each loop
                device.update_state({})
            
            self.display_main_menu()
            choice = self.get_menu_choice()
            
            if choice == 0:
                print("\n🏠 Smart Home System shutting down...")
                print("All devices secured. Have a great day!")
                break
            elif choice == 1:
                self.device_management()
            elif choice == 2:
                self.environmental_monitoring()
            elif choice == 3:
                print("🚧 Security system management coming soon!")
            elif choice == 4:
                print("🚧 Energy management coming soon!")
            elif choice == 5:
                print("🚧 Automation rules coming soon!")
            elif choice == 6:
                print("🚧 System analytics coming soon!")
            elif choice == 7:
                print("🚧 User preferences coming soon!")
            elif choice == 8:
                print("🚧 Emergency systems coming soon!")
            elif choice == 9:
                print("🚧 System diagnostics coming soon!")
            elif choice == 10:
                print("🚧 Integration services coming soon!")
            
            print("\n" + "=" * 70)
            input("Press Enter to continue...")

class LearningEngine:
    """Machine learning-like pattern recognition for automation."""
    
    def __init__(self):
        self.user_patterns = {}
        self.preference_data = []
    
    def learn_user_preferences(self, action: str, context: Dict[str, Any]):
        """Learn from user actions to improve automation."""
        pass  # Implementation would go here

def main():
    """Main entry point for the program."""
    smart_home = SmartHomeSystem()
    smart_home.run()

if __name__ == "__main__":
    main()

"""
SOLUTION REQUIREMENTS:
=====================
Your solution should include:
1. ✅ Complex object-oriented architecture with inheritance
2. ✅ Multi-device management and real-time control systems
3. ✅ Advanced automation rules and intelligent decision making
4. ✅ Environmental monitoring with data analysis and trending
5. ✅ Energy management and optimization algorithms
6. ✅ Security system integration with alert mechanisms
7. ✅ User preference learning and adaptive behavior
8. ✅ Professional IoT system design and implementation

LEARNING OUTCOMES:
==================
After completing this problem, you will have mastered:
• Advanced object-oriented programming with inheritance and polymorphism
• Complex system architecture design and implementation
• Real-time data processing and device control algorithms
• IoT system concepts and smart home automation principles
• Machine learning-like pattern recognition and adaptive systems
• Professional software design for embedded and IoT applications
• Integration of all programming fundamentals in a complex system
• Enterprise-level error handling, logging, and system monitoring

EXTENSION IDEAS:
===============
1. Add voice control integration (Alexa/Google Assistant)
2. Implement mobile app connectivity and remote access
3. Add machine learning for predictive automation
4. Create energy forecasting and cost optimization
5. Implement geofencing for location-based automation
6. Add integration with weather services and external APIs
7. Create advanced security features with facial recognition
8. Add support for additional IoT protocols (Zigbee, Z-Wave)

This expert-level problem integrates ALL course concepts while creating
a sophisticated, real-world applicable smart home automation system!
"""