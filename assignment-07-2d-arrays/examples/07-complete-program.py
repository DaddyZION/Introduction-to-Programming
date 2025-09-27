"""
Assignment 7 - Example 7: Complete 2D Array Program
===================================================

This comprehensive program demonstrates a complete application using 2D arrays
that combines multiple concepts from previous examples. It implements a 
"Smart City Management System" that uses 2D arrays for urban planning,
traffic simulation, resource management, and data analysis.

Key Concepts Demonstrated:
- Complex system design with multiple 2D array structures
- Integration of pathfinding, simulation, and data analysis
- Real-time system state management
- Interactive command-line interface
- Comprehensive error handling and validation
- Performance optimization techniques
- Modular code organization
"""

import random
import time
import math
from collections import deque
from enum import Enum

print("=== SMART CITY MANAGEMENT SYSTEM ===")
print()

print("This program demonstrates a complete 2D array application:")
print("• City grid representation with multiple layers")
print("• Traffic simulation and optimization")
print("• Resource distribution and management")
print("• Population density analysis")
print("• Emergency response planning")
print("• Environmental monitoring")
print("• Statistical reporting and visualization")
print()

# SYSTEM CONSTANTS AND ENUMS
class CellType(Enum):
    """Enumeration for different cell types in the city grid."""
    EMPTY = 0
    RESIDENTIAL = 1
    COMMERCIAL = 2
    INDUSTRIAL = 3
    PARK = 4
    HOSPITAL = 5
    SCHOOL = 6
    POLICE = 7
    FIRE_STATION = 8
    ROAD = 9
    WATER = 10

class TrafficDensity(Enum):
    """Traffic density levels."""
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class ResourceType(Enum):
    """Types of city resources."""
    POWER = 0
    WATER = 1
    WASTE = 2
    INTERNET = 3

# MAIN SMART CITY CLASS
class SmartCity:
    """Complete smart city management system using 2D arrays."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # Multiple 2D array layers for different data
        self.terrain = [[CellType.EMPTY for _ in range(width)] for _ in range(height)]
        self.population_density = [[0 for _ in range(width)] for _ in range(height)]
        self.traffic_flow = [[TrafficDensity.NONE for _ in range(width)] for _ in range(height)]
        self.pollution_levels = [[0.0 for _ in range(width)] for _ in range(height)]
        
        # Resource distribution arrays (4 types of resources)
        self.resources = [[[0 for _ in range(4)] for _ in range(width)] for _ in range(height)]
        
        # Emergency and service coverage
        self.emergency_coverage = [[False for _ in range(width)] for _ in range(height)]
        
        # Time-based data for analytics
        self.time_step = 0
        self.historical_data = []
        
        # System statistics
        self.stats = {
            'total_population': 0,
            'avg_traffic': 0.0,
            'avg_pollution': 0.0,
            'resource_usage': [0, 0, 0, 0],
            'emergency_response_time': 0.0
        }
        
        self.initialize_city()
    
    def initialize_city(self):
        """Initialize the city with basic infrastructure."""
        random.seed(42)  # For reproducible city generation
        
        # Create basic road network (grid pattern)
        self._create_road_network()
        
        # Place essential services
        self._place_essential_services()
        
        # Develop residential and commercial areas
        self._develop_city_zones()
        
        # Initialize resources
        self._initialize_resources()
        
        # Calculate initial coverage areas
        self._update_emergency_coverage()
        
        print("🏙️ Smart City initialized!")
        print(f"   Size: {self.width}×{self.height}")
        print(f"   Population capacity: {self._calculate_population_capacity():,}")
        print()
    
    def _create_road_network(self):
        """Create a basic road network."""
        # Horizontal roads every 4 rows
        for row in range(2, self.height, 6):
            for col in range(self.width):
                self.terrain[row][col] = CellType.ROAD
        
        # Vertical roads every 4 columns
        for col in range(3, self.width, 6):
            for row in range(self.height):
                self.terrain[row][col] = CellType.ROAD
        
        # Add some diagonal connections
        for i in range(min(self.width, self.height) // 8):
            start_row = random.randint(0, self.height - 5)
            start_col = random.randint(0, self.width - 5)
            
            for j in range(4):
                if (start_row + j < self.height and start_col + j < self.width):
                    self.terrain[start_row + j][start_col + j] = CellType.ROAD
    
    def _place_essential_services(self):
        """Place hospitals, schools, police, and fire stations."""
        services = [
            (CellType.HOSPITAL, 3),
            (CellType.SCHOOL, 5),
            (CellType.POLICE, 4),
            (CellType.FIRE_STATION, 3)
        ]
        
        for service_type, count in services:
            placed = 0
            attempts = 0
            
            while placed < count and attempts < 100:
                row = random.randint(1, self.height - 2)
                col = random.randint(1, self.width - 2)
                
                # Prefer locations near roads
                near_road = any(
                    self.terrain[row + dr][col + dc] == CellType.ROAD
                    for dr in [-1, 0, 1] for dc in [-1, 0, 1]
                    if 0 <= row + dr < self.height and 0 <= col + dc < self.width
                )
                
                if self.terrain[row][col] == CellType.EMPTY and near_road:
                    self.terrain[row][col] = service_type
                    placed += 1
                
                attempts += 1
    
    def _develop_city_zones(self):
        """Develop residential, commercial, and industrial zones."""
        zones = [
            (CellType.RESIDENTIAL, 40),
            (CellType.COMMERCIAL, 25),
            (CellType.INDUSTRIAL, 15),
            (CellType.PARK, 10)
        ]
        
        for zone_type, count in zones:
            placed = 0
            attempts = 0
            
            while placed < count and attempts < 200:
                # Try to create clusters
                if placed == 0 or random.random() < 0.3:
                    # New cluster
                    center_row = random.randint(2, self.height - 3)
                    center_col = random.randint(2, self.width - 3)
                else:
                    # Expand existing cluster
                    existing_cells = self._find_cells_of_type(zone_type)
                    if existing_cells:
                        center_row, center_col = random.choice(existing_cells)
                
                # Place 2x2 block
                if self._can_place_block(center_row, center_col, 2, 2):
                    for dr in range(2):
                        for dc in range(2):
                            if (center_row + dr < self.height and 
                                center_col + dc < self.width):
                                self.terrain[center_row + dr][center_col + dc] = zone_type
                    placed += 1
                
                attempts += 1
    
    def _can_place_block(self, start_row, start_col, height, width):
        """Check if a block can be placed at the given location."""
        for row in range(start_row, start_row + height):
            for col in range(start_col, start_col + width):
                if (row >= self.height or col >= self.width or
                    self.terrain[row][col] != CellType.EMPTY):
                    return False
        return True
    
    def _find_cells_of_type(self, cell_type):
        """Find all cells of a specific type."""
        cells = []
        for row in range(self.height):
            for col in range(self.width):
                if self.terrain[row][col] == cell_type:
                    cells.append((row, col))
        return cells
    
    def _initialize_resources(self):
        """Initialize resource distribution."""
        # Power distribution from power plants (industrial areas)
        power_sources = self._find_cells_of_type(CellType.INDUSTRIAL)
        for row, col in power_sources:
            self._distribute_resource(row, col, ResourceType.POWER, radius=8, strength=100)
        
        # Water distribution
        water_sources = [(0, c) for c in range(0, self.width, 10)]  # Top edge water sources
        for row, col in water_sources:
            self._distribute_resource(row, col, ResourceType.WATER, radius=12, strength=100)
        
        # Internet from commercial areas
        internet_sources = self._find_cells_of_type(CellType.COMMERCIAL)
        for row, col in internet_sources:
            self._distribute_resource(row, col, ResourceType.INTERNET, radius=6, strength=80)
    
    def _distribute_resource(self, source_row, source_col, resource_type, radius, strength):
        """Distribute a resource from a source point."""
        resource_idx = resource_type.value
        
        for row in range(max(0, source_row - radius), 
                        min(self.height, source_row + radius + 1)):
            for col in range(max(0, source_col - radius), 
                            min(self.width, source_col + radius + 1)):
                
                distance = math.sqrt((row - source_row)**2 + (col - source_col)**2)
                if distance <= radius:
                    # Resource strength decreases with distance
                    resource_strength = strength * (1 - distance / radius)
                    current_strength = self.resources[row][col][resource_idx]
                    self.resources[row][col][resource_idx] = max(current_strength, resource_strength)
    
    def _update_emergency_coverage(self):
        """Update emergency service coverage areas."""
        # Clear existing coverage
        for row in range(self.height):
            for col in range(self.width):
                self.emergency_coverage[row][col] = False
        
        # Calculate coverage from emergency services
        emergency_services = (
            self._find_cells_of_type(CellType.HOSPITAL) +
            self._find_cells_of_type(CellType.POLICE) +
            self._find_cells_of_type(CellType.FIRE_STATION)
        )
        
        for service_row, service_col in emergency_services:
            # Coverage radius of 6
            for row in range(max(0, service_row - 6), min(self.height, service_row + 7)):
                for col in range(max(0, service_col - 6), min(self.width, service_col + 7)):
                    distance = abs(row - service_row) + abs(col - service_col)  # Manhattan distance
                    if distance <= 6:
                        self.emergency_coverage[row][col] = True
    
    def _calculate_population_capacity(self):
        """Calculate total population capacity of the city."""
        capacity = 0
        residential_cells = self._find_cells_of_type(CellType.RESIDENTIAL)
        capacity += len(residential_cells) * 200  # 200 people per residential cell
        
        commercial_cells = self._find_cells_of_type(CellType.COMMERCIAL)
        capacity += len(commercial_cells) * 50   # 50 workers per commercial cell
        
        return capacity
    
    def simulate_traffic(self):
        """Simulate traffic flow based on city layout."""
        # Reset traffic
        for row in range(self.height):
            for col in range(self.width):
                self.traffic_flow[row][col] = TrafficDensity.NONE
        
        # Generate traffic from residential to commercial/industrial
        residential_cells = self._find_cells_of_type(CellType.RESIDENTIAL)
        commercial_cells = self._find_cells_of_type(CellType.COMMERCIAL)
        industrial_cells = self._find_cells_of_type(CellType.INDUSTRIAL)
        
        work_destinations = commercial_cells + industrial_cells
        
        for res_row, res_col in residential_cells:
            # Find nearest work destination
            if work_destinations:
                nearest_work = min(work_destinations, 
                                 key=lambda dest: abs(res_row - dest[0]) + abs(res_col - dest[1]))
                
                # Simulate traffic along path (simplified)
                self._add_traffic_along_path(res_row, res_col, nearest_work[0], nearest_work[1])
    
    def _add_traffic_along_path(self, start_row, start_col, end_row, end_col):
        """Add traffic along a simplified path between two points."""
        # Simple Manhattan distance path simulation
        current_row, current_col = start_row, start_col
        
        while current_row != end_row or current_col != end_col:
            # Add traffic to current cell if it's a road
            if self.terrain[current_row][current_col] == CellType.ROAD:
                current_traffic = self.traffic_flow[current_row][current_col]
                new_traffic_value = min(current_traffic.value + 1, TrafficDensity.CRITICAL.value)
                self.traffic_flow[current_row][current_col] = TrafficDensity(new_traffic_value)
            
            # Move towards destination
            if current_row < end_row:
                current_row += 1
            elif current_row > end_row:
                current_row -= 1
            elif current_col < end_col:
                current_col += 1
            elif current_col > end_col:
                current_col -= 1
    
    def simulate_pollution(self):
        """Simulate pollution spread from industrial areas."""
        # Reset pollution
        for row in range(self.height):
            for col in range(self.width):
                self.pollution_levels[row][col] = 0.0
        
        # Industrial areas generate pollution
        industrial_cells = self._find_cells_of_type(CellType.INDUSTRIAL)
        
        for ind_row, ind_col in industrial_cells:
            # Pollution spreads in decreasing circles
            for radius in range(1, 8):
                pollution_level = max(0, 100 - radius * 15)  # Decreases with distance
                
                for row in range(max(0, ind_row - radius), 
                                min(self.height, ind_row + radius + 1)):
                    for col in range(max(0, ind_col - radius), 
                                    min(self.width, ind_col + radius + 1)):
                        
                        distance = math.sqrt((row - ind_row)**2 + (col - ind_col)**2)
                        if distance <= radius:
                            current_pollution = self.pollution_levels[row][col]
                            self.pollution_levels[row][col] = max(current_pollution, pollution_level)
        
        # Parks reduce pollution
        park_cells = self._find_cells_of_type(CellType.PARK)
        for park_row, park_col in park_cells:
            # Parks clean air in surrounding area
            for row in range(max(0, park_row - 3), min(self.height, park_row + 4)):
                for col in range(max(0, park_col - 3), min(self.width, park_col + 4)):
                    self.pollution_levels[row][col] *= 0.7  # Reduce pollution by 30%
    
    def update_population(self):
        """Update population density based on city development."""
        for row in range(self.height):
            for col in range(self.width):
                cell_type = self.terrain[row][col]
                
                if cell_type == CellType.RESIDENTIAL:
                    # Population depends on nearby amenities
                    amenity_score = self._calculate_amenity_score(row, col)
                    base_population = 150 + random.randint(-30, 50)
                    self.population_density[row][col] = int(base_population * amenity_score)
                
                elif cell_type == CellType.COMMERCIAL:
                    # Worker population during business hours
                    self.population_density[row][col] = random.randint(20, 80)
                
                elif cell_type == CellType.INDUSTRIAL:
                    # Fewer workers, mostly automated
                    self.population_density[row][col] = random.randint(10, 40)
                
                else:
                    self.population_density[row][col] = 0
    
    def _calculate_amenity_score(self, row, col):
        """Calculate amenity score for a location (affects desirability)."""
        score = 1.0
        search_radius = 5
        
        amenity_weights = {
            CellType.PARK: 0.3,
            CellType.SCHOOL: 0.2,
            CellType.HOSPITAL: 0.2,
            CellType.COMMERCIAL: 0.15,
            CellType.ROAD: 0.1
        }
        
        for amenity_type, weight in amenity_weights.items():
            nearby_count = 0
            for r in range(max(0, row - search_radius), min(self.height, row + search_radius + 1)):
                for c in range(max(0, col - search_radius), min(self.width, col + search_radius + 1)):
                    if self.terrain[r][c] == amenity_type:
                        nearby_count += 1
            
            score += nearby_count * weight
        
        # Pollution penalty
        pollution = self.pollution_levels[row][col]
        if pollution > 50:
            score *= (1 - (pollution - 50) / 200)  # Reduce score based on pollution
        
        return max(0.3, min(2.0, score))  # Clamp between 0.3 and 2.0
    
    def run_simulation_step(self):
        """Run one step of the city simulation."""
        self.time_step += 1
        
        # Update all simulation components
        self.simulate_traffic()
        self.simulate_pollution()
        self.update_population()
        
        # Update statistics
        self._update_statistics()
        
        # Store historical data
        self._record_historical_data()
        
        print(f"⏱️ Simulation step {self.time_step} completed")
    
    def _update_statistics(self):
        """Update city statistics."""
        # Total population
        total_pop = sum(sum(row) for row in self.population_density)
        self.stats['total_population'] = total_pop
        
        # Average traffic density
        road_cells = self._find_cells_of_type(CellType.ROAD)
        if road_cells:
            traffic_sum = sum(self.traffic_flow[row][col].value for row, col in road_cells)
            self.stats['avg_traffic'] = traffic_sum / len(road_cells)
        
        # Average pollution
        total_cells = self.width * self.height
        pollution_sum = sum(sum(row) for row in self.pollution_levels)
        self.stats['avg_pollution'] = pollution_sum / total_cells
        
        # Resource usage
        for resource_idx in range(4):
            usage = sum(
                self.resources[row][col][resource_idx] 
                for row in range(self.height) 
                for col in range(self.width)
            ) / total_cells
            self.stats['resource_usage'][resource_idx] = usage
    
    def _record_historical_data(self):
        """Record current statistics for trend analysis."""
        data_point = {
            'time_step': self.time_step,
            'population': self.stats['total_population'],
            'traffic': self.stats['avg_traffic'],
            'pollution': self.stats['avg_pollution'],
            'resources': self.stats['resource_usage'][:]
        }
        
        self.historical_data.append(data_point)
        
        # Keep only last 50 data points
        if len(self.historical_data) > 50:
            self.historical_data.pop(0)
    
    def display_city_overview(self):
        """Display an overview of the city using ASCII characters."""
        symbols = {
            CellType.EMPTY: '.',
            CellType.RESIDENTIAL: 'R',
            CellType.COMMERCIAL: 'C',
            CellType.INDUSTRIAL: 'I',
            CellType.PARK: 'P',
            CellType.HOSPITAL: 'H',
            CellType.SCHOOL: 'S',
            CellType.POLICE: '👮',
            CellType.FIRE_STATION: '🚒',
            CellType.ROAD: '═',
            CellType.WATER: '~'
        }
        
        print("🗺️ CITY OVERVIEW")
        print("  " + "".join(f"{i%10}" for i in range(self.width)))
        
        for row in range(min(self.height, 20)):  # Show max 20 rows
            row_str = f"{row%10} "
            for col in range(self.width):
                cell_type = self.terrain[row][col]
                symbol = symbols.get(cell_type, '?')
                row_str += symbol
            print(row_str)
        
        if self.height > 20:
            print(f"... ({self.height - 20} more rows)")
        print()
    
    def display_traffic_heatmap(self):
        """Display traffic density as a heatmap."""
        traffic_symbols = {
            TrafficDensity.NONE: '.',
            TrafficDensity.LOW: '▁',
            TrafficDensity.MEDIUM: '▄',
            TrafficDensity.HIGH: '▇',
            TrafficDensity.CRITICAL: '█'
        }
        
        print("🚦 TRAFFIC DENSITY HEATMAP")
        print("  " + "".join(f"{i%10}" for i in range(self.width)))
        
        for row in range(min(self.height, 15)):
            row_str = f"{row%10} "
            for col in range(self.width):
                traffic = self.traffic_flow[row][col]
                symbol = traffic_symbols.get(traffic, '?')
                row_str += symbol
            print(row_str)
        print("Legend: . None, ▁ Low, ▄ Medium, ▇ High, █ Critical")
        print()
    
    def display_pollution_map(self):
        """Display pollution levels."""
        print("🏭 POLLUTION LEVELS")
        print("  " + "".join(f"{i%10}" for i in range(self.width)))
        
        for row in range(min(self.height, 15)):
            row_str = f"{row%10} "
            for col in range(self.width):
                pollution = self.pollution_levels[row][col]
                
                if pollution < 10:
                    symbol = '.'
                elif pollution < 30:
                    symbol = '░'
                elif pollution < 60:
                    symbol = '▒'
                elif pollution < 90:
                    symbol = '▓'
                else:
                    symbol = '█'
                
                row_str += symbol
            print(row_str)
        print("Legend: . Clean, ░ Light, ▒ Moderate, ▓ Heavy, █ Severe")
        print()
    
    def display_statistics(self):
        """Display current city statistics."""
        print("📊 CITY STATISTICS")
        print(f"   Population: {self.stats['total_population']:,}")
        print(f"   Average Traffic: {self.stats['avg_traffic']:.2f}/4")
        print(f"   Average Pollution: {self.stats['avg_pollution']:.1f}%")
        print(f"   Power Coverage: {self.stats['resource_usage'][0]:.1f}%")
        print(f"   Water Coverage: {self.stats['resource_usage'][1]:.1f}%")
        print(f"   Internet Coverage: {self.stats['resource_usage'][2]:.1f}%")
        print()
        
        # Coverage statistics
        covered_cells = sum(sum(row) for row in self.emergency_coverage)
        coverage_percent = (covered_cells / (self.width * self.height)) * 100
        print(f"   Emergency Coverage: {coverage_percent:.1f}%")
        print()
    
    def display_trends(self):
        """Display historical trends."""
        if len(self.historical_data) < 5:
            print("Not enough data for trend analysis")
            return
        
        print("📈 HISTORICAL TRENDS (Last 10 time steps)")
        
        # Show last 10 data points
        recent_data = self.historical_data[-10:]
        
        print("Step | Pop   | Traffic | Pollution")
        print("-----|-------|---------|----------")
        
        for data in recent_data:
            print(f"{data['time_step']:4d} | {data['population']:5d} | "
                  f"{data['traffic']:7.2f} | {data['pollution']:9.1f}")
        
        # Calculate trends
        if len(self.historical_data) >= 5:
            recent_5 = self.historical_data[-5:]
            old_5 = self.historical_data[-10:-5] if len(self.historical_data) >= 10 else recent_5[:len(recent_5)//2]
            
            pop_trend = sum(d['population'] for d in recent_5) / len(recent_5) - sum(d['population'] for d in old_5) / len(old_5)
            pollution_trend = sum(d['pollution'] for d in recent_5) / len(recent_5) - sum(d['pollution'] for d in old_5) / len(old_5)
            
            print(f"\nTrends:")
            print(f"  Population: {'↗️' if pop_trend > 0 else '↘️'} {pop_trend:+.0f} people")
            print(f"  Pollution: {'↗️' if pollution_trend > 0 else '↘️'} {pollution_trend:+.1f} units")
        
        print()
    
    def find_optimal_locations(self, cell_type, count=3):
        """Find optimal locations for new facilities."""
        print(f"🎯 OPTIMAL LOCATIONS FOR {cell_type.name}")
        
        # Score all empty locations
        empty_locations = self._find_cells_of_type(CellType.EMPTY)
        scored_locations = []
        
        for row, col in empty_locations:
            score = self._calculate_location_score(row, col, cell_type)
            scored_locations.append((score, row, col))
        
        # Sort by score (highest first)
        scored_locations.sort(reverse=True)
        
        # Display top locations
        for i, (score, row, col) in enumerate(scored_locations[:count]):
            print(f"  {i+1}. Location ({row}, {col}) - Score: {score:.2f}")
            
            # Explain why this location is good
            reasons = self._explain_location_score(row, col, cell_type)
            for reason in reasons:
                print(f"     • {reason}")
        
        print()
    
    def _calculate_location_score(self, row, col, facility_type):
        """Calculate a score for placing a facility at a location."""
        score = 0.0
        
        if facility_type == CellType.HOSPITAL:
            # Hospitals should be near population centers and roads
            score += self._get_nearby_population(row, col) * 0.001
            score += self._get_road_accessibility(row, col) * 10
            score -= self.pollution_levels[row][col] * 0.01
        
        elif facility_type == CellType.SCHOOL:
            # Schools should be in residential areas, away from pollution
            score += self._get_nearby_residential_count(row, col) * 5
            score += self._get_road_accessibility(row, col) * 5
            score -= self.pollution_levels[row][col] * 0.02
            score += self._get_nearby_park_count(row, col) * 3
        
        elif facility_type == CellType.PARK:
            # Parks should be near residential areas and reduce pollution
            score += self._get_nearby_residential_count(row, col) * 3
            score += self.pollution_levels[row][col] * 0.01  # More valuable in polluted areas
            score -= self._get_nearby_industrial_count(row, col) * 2
        
        return max(0, score)
    
    def _get_nearby_population(self, row, col):
        """Get population count in nearby area."""
        total = 0
        for r in range(max(0, row - 3), min(self.height, row + 4)):
            for c in range(max(0, col - 3), min(self.width, col + 4)):
                total += self.population_density[r][c]
        return total
    
    def _get_road_accessibility(self, row, col):
        """Calculate road accessibility score."""
        min_distance = float('inf')
        road_cells = self._find_cells_of_type(CellType.ROAD)
        
        for r_row, r_col in road_cells:
            distance = abs(row - r_row) + abs(col - r_col)
            min_distance = min(min_distance, distance)
        
        return max(0, 10 - min_distance) if min_distance != float('inf') else 0
    
    def _get_nearby_residential_count(self, row, col):
        """Count residential buildings nearby."""
        count = 0
        for r in range(max(0, row - 4), min(self.height, row + 5)):
            for c in range(max(0, col - 4), min(self.width, col + 5)):
                if self.terrain[r][c] == CellType.RESIDENTIAL:
                    count += 1
        return count
    
    def _get_nearby_park_count(self, row, col):
        """Count parks nearby."""
        count = 0
        for r in range(max(0, row - 3), min(self.height, row + 4)):
            for c in range(max(0, col - 3), min(self.width, col + 4)):
                if self.terrain[r][c] == CellType.PARK:
                    count += 1
        return count
    
    def _get_nearby_industrial_count(self, row, col):
        """Count industrial buildings nearby."""
        count = 0
        for r in range(max(0, row - 5), min(self.height, row + 6)):
            for c in range(max(0, col - 5), min(self.width, col + 6)):
                if self.terrain[r][c] == CellType.INDUSTRIAL:
                    count += 1
        return count
    
    def _explain_location_score(self, row, col, facility_type):
        """Provide human-readable explanation for location score."""
        reasons = []
        
        nearby_pop = self._get_nearby_population(row, col)
        road_access = self._get_road_accessibility(row, col)
        pollution = self.pollution_levels[row][col]
        
        if nearby_pop > 500:
            reasons.append(f"High population density nearby ({nearby_pop} people)")
        elif nearby_pop > 200:
            reasons.append(f"Moderate population density nearby ({nearby_pop} people)")
        
        if road_access > 7:
            reasons.append("Excellent road access")
        elif road_access > 4:
            reasons.append("Good road access")
        
        if pollution < 20:
            reasons.append("Low pollution area")
        elif pollution > 60:
            reasons.append("High pollution - needs environmental services")
        
        if facility_type == CellType.SCHOOL:
            park_count = self._get_nearby_park_count(row, col)
            if park_count > 0:
                reasons.append(f"Near {park_count} park(s) - good for children")
        
        return reasons[:3]  # Return top 3 reasons

# INTERACTIVE MENU SYSTEM
def run_smart_city_simulation():
    """Run the interactive smart city simulation."""
    print("🌟 Welcome to the Smart City Management System!")
    print()
    
    # Initialize city
    city_width = 30
    city_height = 20
    city = SmartCity(city_width, city_height)
    
    while True:
        print("=== SMART CITY CONTROL PANEL ===")
        print("1. View City Overview")
        print("2. View Traffic Heatmap")
        print("3. View Pollution Map")
        print("4. View Statistics")
        print("5. View Historical Trends")
        print("6. Run Simulation Step")
        print("7. Run Multiple Steps")
        print("8. Find Optimal Hospital Locations")
        print("9. Find Optimal School Locations")
        print("10. Find Optimal Park Locations")
        print("11. Emergency Response Analysis")
        print("0. Exit")
        print()
        
        try:
            choice = input("Enter your choice (0-11): ").strip()
            
            if choice == '0':
                print("👋 Thank you for using Smart City Management System!")
                break
            
            elif choice == '1':
                city.display_city_overview()
            
            elif choice == '2':
                city.display_traffic_heatmap()
            
            elif choice == '3':
                city.display_pollution_map()
            
            elif choice == '4':
                city.display_statistics()
            
            elif choice == '5':
                city.display_trends()
            
            elif choice == '6':
                city.run_simulation_step()
            
            elif choice == '7':
                try:
                    steps = int(input("How many steps to simulate? (1-10): "))
                    steps = max(1, min(10, steps))
                    
                    print(f"Running {steps} simulation steps...")
                    for i in range(steps):
                        city.run_simulation_step()
                        if i < steps - 1:
                            time.sleep(0.5)  # Brief pause between steps
                    
                    print(f"✅ Completed {steps} simulation steps")
                except ValueError:
                    print("❌ Invalid number of steps")
            
            elif choice == '8':
                city.find_optimal_locations(CellType.HOSPITAL)
            
            elif choice == '9':
                city.find_optimal_locations(CellType.SCHOOL)
            
            elif choice == '10':
                city.find_optimal_locations(CellType.PARK)
            
            elif choice == '11':
                emergency_response_analysis(city)
            
            else:
                print("❌ Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
        
        print()
        input("Press Enter to continue...")
        print()

def emergency_response_analysis(city):
    """Analyze emergency response coverage and times."""
    print("🚨 EMERGENCY RESPONSE ANALYSIS")
    
    # Find emergency services
    hospitals = city._find_cells_of_type(CellType.HOSPITAL)
    police = city._find_cells_of_type(CellType.POLICE)
    fire_stations = city._find_cells_of_type(CellType.FIRE_STATION)
    
    print(f"Emergency Services Available:")
    print(f"  🏥 Hospitals: {len(hospitals)}")
    print(f"  👮 Police Stations: {len(police)}")
    print(f"  🚒 Fire Stations: {len(fire_stations)}")
    print()
    
    # Calculate coverage
    covered_cells = sum(sum(row) for row in city.emergency_coverage)
    total_cells = city.width * city.height
    coverage_percent = (covered_cells / total_cells) * 100
    
    print(f"Coverage Statistics:")
    print(f"  Total Coverage: {coverage_percent:.1f}%")
    print(f"  Covered Area: {covered_cells} cells")
    print(f"  Uncovered Area: {total_cells - covered_cells} cells")
    print()
    
    # Find areas with poor coverage
    uncovered_residential = []
    for row in range(city.height):
        for col in range(city.width):
            if (city.terrain[row][col] == CellType.RESIDENTIAL and 
                not city.emergency_coverage[row][col]):
                uncovered_residential.append((row, col))
    
    if uncovered_residential:
        print(f"⚠️  Uncovered Residential Areas: {len(uncovered_residential)}")
        print("   Top priority locations for new emergency services:")
        
        # Show first few uncovered residential areas
        for i, (row, col) in enumerate(uncovered_residential[:5]):
            population = city.population_density[row][col]
            print(f"     {i+1}. ({row}, {col}) - {population} residents")
    else:
        print("✅ All residential areas have emergency coverage!")
    
    print()

# MAIN EXECUTION
if __name__ == "__main__":
    print("Starting Smart City Management System...")
    print()
    run_smart_city_simulation()

"""
PROGRAM FEATURES DEMONSTRATED:
==============================
1. Multiple 2D Array Layers:
   - Terrain/building types
   - Population density
   - Traffic flow patterns
   - Pollution levels
   - Resource distribution (4 types)
   - Emergency service coverage

2. Complex Algorithms:
   - Pathfinding for traffic simulation
   - Resource distribution algorithms
   - Pollution spread modeling
   - Location optimization scoring
   - Statistical trend analysis

3. Real-time Simulation:
   - Multi-step simulation updates
   - Historical data tracking
   - Dynamic system state changes
   - Interactive parameter adjustment

4. Data Visualization:
   - ASCII art city maps
   - Traffic density heatmaps
   - Pollution level displays
   - Statistical trend charts
   - Coverage area analysis

5. Interactive Interface:
   - Menu-driven command system
   - Real-time user input handling
   - Error handling and validation
   - User-friendly feedback

6. Advanced Features:
   - Multi-criteria decision analysis
   - Spatial relationship calculations
   - Time-series data analysis
   - Emergency response planning
   - Urban planning optimization

KEY PROGRAMMING CONCEPTS:
=========================
• 2D Array Manipulation: Multiple arrays for different data layers
• Object-Oriented Design: Modular, maintainable code structure
• Algorithm Implementation: Pathfinding, optimization, simulation
• Data Analysis: Statistics, trends, correlation analysis
• User Interface Design: Interactive menus, error handling
• System Integration: Combining multiple subsystems
• Performance Optimization: Efficient array operations
• Real-world Modeling: Simulating complex urban systems

EDUCATIONAL VALUE:
==================
This complete program demonstrates how 2D arrays can be used to build
sophisticated applications that model real-world systems. It combines
multiple programming concepts and shows how arrays form the foundation
for complex data management and analysis tasks.

The Smart City Management System illustrates practical applications of:
- Urban planning and development
- Traffic engineering and optimization  
- Environmental monitoring and control
- Resource allocation and management
- Emergency services planning
- Data-driven decision making
- Statistical analysis and reporting

This capstone example shows students how individual programming concepts
come together to create meaningful, real-world applications that could
actually be used by city planners, government officials, and urban
development professionals.
"""