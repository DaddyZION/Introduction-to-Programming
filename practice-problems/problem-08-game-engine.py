"""
Practice Problem 08: Game Development Engine
==========================================

DIFFICULTY: Expert ⭐⭐⭐⭐
CONCEPTS: Advanced Programming Integration, Game Logic, Data Structures
ASSIGNMENTS: Complete integration of all assignments (1-7)
ESTIMATED TIME: 130-160 minutes

PROBLEM DESCRIPTION:
===================
Create a comprehensive 2D game development engine that supports multiple game types,
sprite management, collision detection, scoring systems, and AI opponents. The engine
should be flexible enough to create different types of games while providing a
robust foundation for game mechanics, graphics simulation, and player interaction.

This expert problem integrates all programming concepts including complex algorithms,
data structures, object-oriented design, and real-time game logic processing.

REQUIREMENTS:
============
1. Game engine architecture with modular components
2. Multiple game types (puzzle, arcade, strategy)
3. Sprite and animation management systems
4. Physics simulation and collision detection
5. AI opponent behavior and pathfinding
6. Scoring, achievements, and player progression
7. Game state management and save/load functionality
8. Sound effects simulation and game audio management

LEARNING OBJECTIVES:
===================
- Master advanced software architecture and design patterns
- Understand game development principles and real-time systems
- Practice complex algorithm implementation and optimization
- Implement AI and machine learning concepts
- Design professional game development tools and engines
- Work with advanced data structures and memory management

STARTER CODE:
============
"""

import random
import math
import json
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional, Any
from enum import Enum
from abc import ABC, abstractmethod

class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    VICTORY = "victory"
    SETTINGS = "settings"

class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    NONE = "none"

class CollisionType(Enum):
    NONE = "none"
    WALL = "wall"
    ENEMY = "enemy"
    PICKUP = "pickup"
    BOUNDARY = "boundary"

class Vector2D:
    """2D vector class for position and movement calculations."""
    
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self) -> 'Vector2D':
        mag = self.magnitude()
        if mag > 0:
            return Vector2D(self.x / mag, self.y / mag)
        return Vector2D(0, 0)
    
    def distance_to(self, other: 'Vector2D') -> float:
        return (self - other).magnitude()
    
    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"

class GameObject(ABC):
    """Abstract base class for all game objects."""
    
    def __init__(self, position: Vector2D, size: Vector2D, game_type: str):
        self.position = position
        self.size = size
        self.velocity = Vector2D(0, 0)
        self.game_type = game_type
        self.active = True
        self.visible = True
        self.collidable = True
        self.health = 100.0
        self.max_health = 100.0
        self.created_time = datetime.now()
        self.last_update = datetime.now()
    
    @abstractmethod
    def update(self, delta_time: float, game_world: 'GameWorld'):
        """Update object state each frame."""
        pass
    
    @abstractmethod
    def render(self) -> str:
        """Return text representation for rendering."""
        pass
    
    def get_bounds(self) -> Dict[str, float]:
        """Get bounding box for collision detection."""
        return {
            'left': self.position.x - self.size.x / 2,
            'right': self.position.x + self.size.x / 2,
            'top': self.position.y - self.size.y / 2,
            'bottom': self.position.y + self.size.y / 2
        }
    
    def intersects_with(self, other: 'GameObject') -> bool:
        """Check if this object intersects with another."""
        self_bounds = self.get_bounds()
        other_bounds = other.get_bounds()
        
        return not (self_bounds['right'] < other_bounds['left'] or
                   self_bounds['left'] > other_bounds['right'] or
                   self_bounds['bottom'] < other_bounds['top'] or
                   self_bounds['top'] > other_bounds['bottom'])
    
    def take_damage(self, damage: float):
        """Apply damage to the object."""
        self.health = max(0, self.health - damage)
        if self.health <= 0:
            self.active = False

class Player(GameObject):
    """Player character class."""
    
    def __init__(self, position: Vector2D, game_type: str):
        super().__init__(position, Vector2D(2, 2), game_type)
        self.speed = 5.0
        self.direction = Direction.NONE
        self.score = 0
        self.lives = 3
        self.power_up_time = 0.0
        self.invulnerable_time = 0.0
        self.abilities = []
        self.inventory = {}
        
    def update(self, delta_time: float, game_world: 'GameWorld'):
        """Update player state."""
        self.last_update = datetime.now()
        
        # Update timers
        self.power_up_time = max(0, self.power_up_time - delta_time)
        self.invulnerable_time = max(0, self.invulnerable_time - delta_time)
        
        # Apply movement based on direction
        movement = Vector2D(0, 0)
        
        if self.direction == Direction.UP:
            movement.y = -self.speed
        elif self.direction == Direction.DOWN:
            movement.y = self.speed
        elif self.direction == Direction.LEFT:
            movement.x = -self.speed
        elif self.direction == Direction.RIGHT:
            movement.x = self.speed
        
        # Update position
        self.velocity = movement
        self.position = self.position + (self.velocity * delta_time)
        
        # Keep player within bounds
        game_world.clamp_to_bounds(self)
        
    def render(self) -> str:
        """Render player character."""
        if self.invulnerable_time > 0:
            return "😵‍💫" if int(self.invulnerable_time * 10) % 2 else "😊"
        elif self.power_up_time > 0:
            return "⭐"
        else:
            return "😊"
    
    def move(self, direction: Direction):
        """Set player movement direction."""
        self.direction = direction
    
    def stop(self):
        """Stop player movement."""
        self.direction = Direction.NONE
    
    def add_score(self, points: int):
        """Add points to player score."""
        self.score += points
    
    def activate_power_up(self, power_type: str, duration: float):
        """Activate a power-up."""
        self.power_up_time = duration
        self.abilities.append(power_type)
    
    def lose_life(self):
        """Player loses a life."""
        self.lives = max(0, self.lives - 1)
        self.invulnerable_time = 2.0  # 2 seconds of invulnerability
        
        if self.lives <= 0:
            self.active = False

class Enemy(GameObject):
    """Enemy AI class with different behavior patterns."""
    
    def __init__(self, position: Vector2D, enemy_type: str, game_type: str):
        super().__init__(position, Vector2D(2, 2), game_type)
        self.enemy_type = enemy_type
        self.speed = random.uniform(1.0, 3.0)
        self.ai_state = "patrol"
        self.target = None
        self.patrol_points = []
        self.current_patrol_index = 0
        self.last_direction_change = 0.0
        self.attack_damage = 10.0
        self.detection_range = 8.0
        self.attack_cooldown = 0.0
        
        # Set up different enemy types
        self.setup_enemy_type()
        
    def setup_enemy_type(self):
        """Configure enemy based on type."""
        if self.enemy_type == "guard":
            self.speed = 2.0
            self.attack_damage = 15.0
            self.detection_range = 6.0
            self.health = 50.0
            self.max_health = 50.0
            
        elif self.enemy_type == "scout":
            self.speed = 4.0
            self.attack_damage = 8.0
            self.detection_range = 10.0
            self.health = 30.0
            self.max_health = 30.0
            
        elif self.enemy_type == "boss":
            self.speed = 1.5
            self.attack_damage = 25.0
            self.detection_range = 12.0
            self.health = 200.0
            self.max_health = 200.0
            self.size = Vector2D(4, 4)
    
    def update(self, delta_time: float, game_world: 'GameWorld'):
        """Update enemy AI behavior."""
        self.last_update = datetime.now()
        self.attack_cooldown = max(0, self.attack_cooldown - delta_time)
        
        # Find player
        player = game_world.get_player()
        if player and player.active:
            distance_to_player = self.position.distance_to(player.position)
            
            # State machine for AI behavior
            if distance_to_player <= self.detection_range:
                if self.ai_state != "attack":
                    self.ai_state = "chase"
                    self.target = player
            elif self.ai_state == "chase":
                self.ai_state = "patrol"
                self.target = None
            
            # Execute behavior based on state
            if self.ai_state == "chase":
                self.chase_target(player, delta_time)
            elif self.ai_state == "attack":
                self.attack_target(player, delta_time, game_world)
            else:
                self.patrol_behavior(delta_time)
        else:
            self.patrol_behavior(delta_time)
        
        # Apply movement
        self.position = self.position + (self.velocity * delta_time)
        game_world.clamp_to_bounds(self)
    
    def chase_target(self, target: GameObject, delta_time: float):
        """Chase behavior - move toward target."""
        direction_to_target = (target.position - self.position).normalize()
        self.velocity = direction_to_target * self.speed
        
        # Check if close enough to attack
        if self.position.distance_to(target.position) <= 3.0 and self.attack_cooldown <= 0:
            self.ai_state = "attack"
    
    def attack_target(self, target: GameObject, delta_time: float, game_world: 'GameWorld'):
        """Attack behavior - damage target if in range."""
        if self.position.distance_to(target.position) <= 3.0:
            if isinstance(target, Player) and target.invulnerable_time <= 0:
                target.take_damage(self.attack_damage)
                target.lose_life()
                game_world.create_effect("damage", target.position)
            
            self.attack_cooldown = 1.0  # 1 second cooldown
            self.ai_state = "chase"
        else:
            self.ai_state = "chase"
    
    def patrol_behavior(self, delta_time: float):
        """Patrol behavior - random movement."""
        self.last_direction_change += delta_time
        
        if self.last_direction_change >= 2.0:  # Change direction every 2 seconds
            angle = random.uniform(0, 2 * math.pi)
            direction = Vector2D(math.cos(angle), math.sin(angle))
            self.velocity = direction * self.speed
            self.last_direction_change = 0.0
    
    def render(self) -> str:
        """Render enemy based on type and state."""
        if self.enemy_type == "guard":
            return "👮" if self.ai_state == "patrol" else "😡"
        elif self.enemy_type == "scout":
            return "🏃" if self.ai_state == "patrol" else "🔍"
        elif self.enemy_type == "boss":
            return "👹" if self.ai_state == "patrol" else "😈"
        else:
            return "👾"

class Pickup(GameObject):
    """Collectible items for the player."""
    
    def __init__(self, position: Vector2D, pickup_type: str, game_type: str):
        super().__init__(position, Vector2D(1, 1), game_type)
        self.pickup_type = pickup_type
        self.value = 0
        self.effect_duration = 0.0
        self.bob_offset = 0.0
        self.bob_speed = 3.0
        
        self.setup_pickup_type()
    
    def setup_pickup_type(self):
        """Configure pickup based on type."""
        if self.pickup_type == "coin":
            self.value = 10
        elif self.pickup_type == "gem":
            self.value = 50
        elif self.pickup_type == "health":
            self.value = 25
        elif self.pickup_type == "power_up":
            self.effect_duration = 5.0
        elif self.pickup_type == "speed_boost":
            self.effect_duration = 8.0
        elif self.pickup_type == "shield":
            self.effect_duration = 10.0
    
    def update(self, delta_time: float, game_world: 'GameWorld'):
        """Update pickup animation and check for collection."""
        self.last_update = datetime.now()
        
        # Bobbing animation
        self.bob_offset += self.bob_speed * delta_time
        
        # Check for collection by player
        player = game_world.get_player()
        if player and player.active and self.intersects_with(player):
            self.collect(player, game_world)
    
    def collect(self, player: Player, game_world: 'GameWorld'):
        """Handle collection by player."""
        if self.pickup_type in ["coin", "gem"]:
            player.add_score(self.value)
            game_world.create_effect("score", self.position, str(self.value))
            
        elif self.pickup_type == "health":
            player.health = min(player.max_health, player.health + self.value)
            game_world.create_effect("heal", self.position)
            
        elif self.pickup_type == "power_up":
            player.activate_power_up("power", self.effect_duration)
            game_world.create_effect("power", self.position)
            
        elif self.pickup_type == "speed_boost":
            player.speed *= 1.5
            game_world.create_effect("speed", self.position)
            
        elif self.pickup_type == "shield":
            player.invulnerable_time = self.effect_duration
            game_world.create_effect("shield", self.position)
        
        # Remove pickup from game world
        self.active = False
    
    def render(self) -> str:
        """Render pickup with bobbing effect."""
        # Simple bobbing effect using modulo
        bob_frame = int(self.bob_offset) % 2
        
        if self.pickup_type == "coin":
            return "🪙" if bob_frame == 0 else "💰"
        elif self.pickup_type == "gem":
            return "💎" if bob_frame == 0 else "✨"
        elif self.pickup_type == "health":
            return "❤️" if bob_frame == 0 else "💗"
        elif self.pickup_type == "power_up":
            return "⭐" if bob_frame == 0 else "🌟"
        elif self.pickup_type == "speed_boost":
            return "⚡" if bob_frame == 0 else "🔋"
        elif self.pickup_type == "shield":
            return "🛡️" if bob_frame == 0 else "🔰"
        else:
            return "❓"

class GameWorld:
    """Game world containing all game objects and logic."""
    
    def __init__(self, width: int, height: int, game_type: str):
        self.width = width
        self.height = height
        self.game_type = game_type
        self.objects = []
        self.effects = []
        self.player = None
        self.enemies = []
        self.pickups = []
        self.walls = []
        self.game_state = GameState.MENU
        self.level = 1
        self.time_remaining = 60.0  # 1 minute per level
        self.wave_number = 1
        
        # Game statistics
        self.total_enemies_defeated = 0
        self.total_pickups_collected = 0
        self.level_start_time = datetime.now()
        
    def add_object(self, obj: GameObject):
        """Add object to the game world."""
        self.objects.append(obj)
        
        if isinstance(obj, Player):
            self.player = obj
        elif isinstance(obj, Enemy):
            self.enemies.append(obj)
        elif isinstance(obj, Pickup):
            self.pickups.append(obj)
    
    def remove_object(self, obj: GameObject):
        """Remove object from the game world."""
        if obj in self.objects:
            self.objects.remove(obj)
        
        if isinstance(obj, Enemy) and obj in self.enemies:
            self.enemies.remove(obj)
            self.total_enemies_defeated += 1
        elif isinstance(obj, Pickup) and obj in self.pickups:
            self.pickups.remove(obj)
            self.total_pickups_collected += 1
    
    def get_player(self) -> Optional[Player]:
        """Get the player object."""
        return self.player
    
    def update(self, delta_time: float):
        """Update all game objects."""
        # Update all objects
        for obj in self.objects[:]:  # Use slice to avoid modification during iteration
            if obj.active:
                obj.update(delta_time, self)
            else:
                self.remove_object(obj)
        
        # Update effects
        for effect in self.effects[:]:
            effect['duration'] -= delta_time
            if effect['duration'] <= 0:
                self.effects.remove(effect)
        
        # Update game timers
        if self.game_state == GameState.PLAYING:
            self.time_remaining -= delta_time
            
            # Check win/lose conditions
            self.check_game_conditions()
    
    def check_game_conditions(self):
        """Check for win/lose conditions."""
        if self.player and not self.player.active:
            self.game_state = GameState.GAME_OVER
        elif self.time_remaining <= 0:
            if len(self.enemies) == 0:
                self.game_state = GameState.VICTORY
            else:
                self.game_state = GameState.GAME_OVER
        elif len(self.enemies) == 0 and self.game_type == "survival":
            # Spawn next wave
            self.spawn_enemy_wave()
    
    def spawn_enemy_wave(self):
        """Spawn a new wave of enemies."""
        self.wave_number += 1
        enemy_count = min(10, 2 + self.wave_number)
        
        for _ in range(enemy_count):
            # Random spawn position at edges
            if random.choice([True, False]):
                x = random.choice([2, self.width - 2])
                y = random.uniform(2, self.height - 2)
            else:
                x = random.uniform(2, self.width - 2)
                y = random.choice([2, self.height - 2])
            
            position = Vector2D(x, y)
            enemy_type = random.choice(["guard", "scout"])
            
            # Add boss every 5 waves
            if self.wave_number % 5 == 0:
                enemy_type = "boss"
            
            enemy = Enemy(position, enemy_type, self.game_type)
            self.add_object(enemy)
        
        # Add bonus time for each wave
        self.time_remaining += 30.0
    
    def clamp_to_bounds(self, obj: GameObject):
        """Keep object within world boundaries."""
        half_width = obj.size.x / 2
        half_height = obj.size.y / 2
        
        obj.position.x = max(half_width, min(self.width - half_width, obj.position.x))
        obj.position.y = max(half_height, min(self.height - half_height, obj.position.y))
    
    def create_effect(self, effect_type: str, position: Vector2D, text: str = ""):
        """Create visual effect at position."""
        effect = {
            'type': effect_type,
            'position': position,
            'text': text,
            'duration': 1.0,
            'created': datetime.now()
        }
        self.effects.append(effect)
    
    def get_display_grid(self) -> List[List[str]]:
        """Generate display grid for rendering."""
        grid = [["." for _ in range(self.width)] for _ in range(self.height)]
        
        # Render all objects
        for obj in self.objects:
            if obj.visible and obj.active:
                x = int(obj.position.x)
                y = int(obj.position.y)
                
                if 0 <= x < self.width and 0 <= y < self.height:
                    grid[y][x] = obj.render()
        
        # Render effects
        for effect in self.effects:
            x = int(effect['position'].x)
            y = int(effect['position'].y)
            
            if 0 <= x < self.width and 0 <= y < self.height:
                if effect['type'] == 'damage':
                    grid[y][x] = "💥"
                elif effect['type'] == 'heal':
                    grid[y][x] = "✨"
                elif effect['type'] == 'power':
                    grid[y][x] = "🌟"
                elif effect['type'] == 'speed':
                    grid[y][x] = "💨"
                elif effect['type'] == 'shield':
                    grid[y][x] = "🔮"
        
        return grid

class GameEngine:
    """Main game engine managing all game systems."""
    
    def __init__(self):
        """Initialize the game engine."""
        self.current_game = None
        self.game_types = {
            "maze_runner": "Navigate mazes while avoiding enemies",
            "survival": "Survive waves of enemies as long as possible", 
            "treasure_hunt": "Collect all treasures while managing resources",
            "boss_battle": "Face increasingly difficult boss enemies"
        }
        self.high_scores = {}
        self.player_stats = {
            'games_played': 0,
            'total_score': 0,
            'best_survival_time': 0,
            'total_enemies_defeated': 0,
            'achievements': []
        }
        
        # Load saved data
        self.load_game_data()
    
    def display_main_menu(self):
        """Display the main game engine menu."""
        print("=" * 70)
        print("                    GAME DEVELOPMENT ENGINE")
        print("=" * 70)
        print("🎮 Available Games:")
        
        for i, (game_id, description) in enumerate(self.game_types.items(), 1):
            print(f"{i}. {game_id.replace('_', ' ').title()}")
            print(f"   {description}")
            if game_id in self.high_scores:
                print(f"   🏆 High Score: {self.high_scores[game_id]}")
            print()
        
        print("📊 Other Options:")
        print(f"{len(self.game_types) + 1}. View Player Statistics")
        print(f"{len(self.game_types) + 2}. Game Development Tools")
        print(f"{len(self.game_types) + 3}. Achievement Gallery")
        print("0. Exit")
        print("=" * 70)
    
    def get_menu_choice(self):
        """Get and validate user's menu choice."""
        max_choice = len(self.game_types) + 3
        
        while True:
            try:
                choice = int(input(f"Enter your choice (0-{max_choice}): "))
                if 0 <= choice <= max_choice:
                    return choice
                else:
                    print(f"❌ Please enter a number between 0 and {max_choice}.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def create_game(self, game_type: str) -> GameWorld:
        """Create a new game world based on type."""
        world = GameWorld(40, 20, game_type)
        
        # Create player at center
        player_pos = Vector2D(world.width // 2, world.height // 2)
        player = Player(player_pos, game_type)
        world.add_object(player)
        
        if game_type == "maze_runner":
            self.setup_maze_runner(world)
        elif game_type == "survival":
            self.setup_survival(world)
        elif game_type == "treasure_hunt":
            self.setup_treasure_hunt(world)
        elif game_type == "boss_battle":
            self.setup_boss_battle(world)
        
        world.game_state = GameState.PLAYING
        return world
    
    def setup_maze_runner(self, world: GameWorld):
        """Set up maze runner game."""
        # Add some enemies
        for i in range(5):
            x = random.uniform(5, world.width - 5)
            y = random.uniform(5, world.height - 5)
            enemy = Enemy(Vector2D(x, y), "guard", "maze_runner")
            world.add_object(enemy)
        
        # Add pickups
        for i in range(10):
            x = random.uniform(3, world.width - 3)
            y = random.uniform(3, world.height - 3)
            pickup_type = random.choice(["coin", "gem", "health"])
            pickup = Pickup(Vector2D(x, y), pickup_type, "maze_runner")
            world.add_object(pickup)
        
        world.time_remaining = 120.0  # 2 minutes
    
    def setup_survival(self, world: GameWorld):
        """Set up survival game."""
        # Start with fewer enemies, more will spawn in waves
        for i in range(3):
            x = random.uniform(5, world.width - 5)
            y = random.uniform(5, world.height - 5)
            enemy = Enemy(Vector2D(x, y), "scout", "survival")
            world.add_object(enemy)
        
        # Add health pickups
        for i in range(5):
            x = random.uniform(3, world.width - 3)
            y = random.uniform(3, world.height - 3)
            pickup = Pickup(Vector2D(x, y), "health", "survival")
            world.add_object(pickup)
        
        world.time_remaining = 300.0  # 5 minutes initial
    
    def setup_treasure_hunt(self, world: GameWorld):
        """Set up treasure hunt game."""
        # Add guards
        for i in range(4):
            x = random.uniform(5, world.width - 5)
            y = random.uniform(5, world.height - 5)
            enemy = Enemy(Vector2D(x, y), "guard", "treasure_hunt")
            world.add_object(enemy)
        
        # Add treasures (gems and coins)
        for i in range(15):
            x = random.uniform(3, world.width - 3)
            y = random.uniform(3, world.height - 3)
            pickup_type = random.choice(["coin", "gem"])
            pickup = Pickup(Vector2D(x, y), pickup_type, "treasure_hunt")
            world.add_object(pickup)
        
        world.time_remaining = 180.0  # 3 minutes
    
    def setup_boss_battle(self, world: GameWorld):
        """Set up boss battle game."""
        # Add boss enemy
        boss_pos = Vector2D(world.width - 10, world.height // 2)
        boss = Enemy(boss_pos, "boss", "boss_battle")
        world.add_object(boss)
        
        # Add some minions
        for i in range(2):
            x = random.uniform(world.width - 15, world.width - 5)
            y = random.uniform(5, world.height - 5)
            enemy = Enemy(Vector2D(x, y), "scout", "boss_battle")
            world.add_object(enemy)
        
        # Add power-ups
        for i in range(8):
            x = random.uniform(3, world.width - 3)
            y = random.uniform(3, world.height - 3)
            pickup_type = random.choice(["health", "power_up", "shield"])
            pickup = Pickup(Vector2D(x, y), pickup_type, "boss_battle")
            world.add_object(pickup)
        
        world.time_remaining = 240.0  # 4 minutes
    
    def play_game(self, game_type: str):
        """Main game loop."""
        print(f"\n🎮 Starting {game_type.replace('_', ' ').title()}...")
        print("Controls: WASD to move, Q to quit, P to pause")
        print("=" * 50)
        
        world = self.create_game(game_type)
        frame_time = 0.1  # 10 FPS simulation
        last_input_time = datetime.now()
        
        while world.game_state == GameState.PLAYING:
            # Clear screen (simulate)
            print("\n" * 3)
            
            # Update game world
            world.update(frame_time)
            
            # Render game
            self.render_game(world)
            
            # Get player input (simplified)
            print("\nEnter command (w/a/s/d to move, q to quit, p to pause): ", end="")
            
            # Simulate real-time input (in a real game, this would be event-driven)
            try:
                import sys, select
                
                # Simplified input handling
                command = input().lower().strip()
                
                if command == 'q':
                    world.game_state = GameState.GAME_OVER
                elif command == 'p':
                    world.game_state = GameState.PAUSED
                    print("Game paused. Press any key to continue...")
                    input()
                    world.game_state = GameState.PLAYING
                elif command in ['w', 'a', 's', 'd']:
                    direction_map = {
                        'w': Direction.UP,
                        's': Direction.DOWN, 
                        'a': Direction.LEFT,
                        'd': Direction.RIGHT
                    }
                    
                    if world.player:
                        world.player.move(direction_map[command])
                
            except KeyboardInterrupt:
                break
            except:
                # Continue without input
                if world.player:
                    world.player.stop()
            
            # Simulate frame timing
            import time
            time.sleep(frame_time)
        
        # Game ended
        self.handle_game_end(world)
    
    def render_game(self, world: GameWorld):
        """Render the current game state."""
        grid = world.get_display_grid()
        
        # Print top border
        print("+" + "-" * world.width + "+")
        
        # Print game grid
        for row in grid:
            print("|" + "".join(row) + "|")
        
        # Print bottom border
        print("+" + "-" * world.width + "+")
        
        # Print game UI
        if world.player:
            print(f"Score: {world.player.score} | Lives: {world.player.lives} | "
                  f"Health: {world.player.health:.0f} | Time: {world.time_remaining:.0f}s")
            
            if world.game_type == "survival":
                print(f"Wave: {world.wave_number} | Enemies: {len(world.enemies)}")
            
            if world.player.power_up_time > 0:
                print(f"⭐ Power-up: {world.player.power_up_time:.1f}s remaining")
            
            if world.player.invulnerable_time > 0:
                print(f"🛡️ Invulnerable: {world.player.invulnerable_time:.1f}s remaining")
    
    def handle_game_end(self, world: GameWorld):
        """Handle end of game - scoring, achievements, etc."""
        self.player_stats['games_played'] += 1
        
        if world.player:
            final_score = world.player.score
            self.player_stats['total_score'] += final_score
            self.player_stats['total_enemies_defeated'] += world.total_enemies_defeated
            
            # Check for high score
            game_type = world.game_type
            if game_type not in self.high_scores or final_score > self.high_scores[game_type]:
                self.high_scores[game_type] = final_score
                print(f"\n🏆 NEW HIGH SCORE: {final_score}!")
            
            # Check for achievements
            self.check_achievements(world)
            
            print(f"\n📊 GAME OVER")
            print("=" * 30)
            print(f"Final Score: {final_score}")
            print(f"Survival Time: {(datetime.now() - world.level_start_time).seconds}s")
            print(f"Enemies Defeated: {world.total_enemies_defeated}")
            print(f"Pickups Collected: {world.total_pickups_collected}")
            
            if world.game_state == GameState.VICTORY:
                print("🎉 VICTORY! You completed the level!")
            else:
                print("💀 Game Over! Better luck next time!")
        
        # Save game data
        self.save_game_data()
        
        input("\nPress Enter to return to main menu...")
    
    def check_achievements(self, world: GameWorld):
        """Check and award achievements."""
        achievements = []
        
        if world.player.score >= 1000 and "high_scorer" not in self.player_stats['achievements']:
            achievements.append("high_scorer")
            print("🏆 Achievement Unlocked: High Scorer!")
        
        if world.total_enemies_defeated >= 10 and "enemy_hunter" not in self.player_stats['achievements']:
            achievements.append("enemy_hunter")
            print("🏆 Achievement Unlocked: Enemy Hunter!")
        
        if world.total_pickups_collected >= 20 and "collector" not in self.player_stats['achievements']:
            achievements.append("collector")
            print("🏆 Achievement Unlocked: Collector!")
        
        survival_time = (datetime.now() - world.level_start_time).seconds
        if survival_time >= 300 and "survivor" not in self.player_stats['achievements']:
            achievements.append("survivor")
            print("🏆 Achievement Unlocked: Survivor!")
        
        # Add new achievements to player stats
        for achievement in achievements:
            if achievement not in self.player_stats['achievements']:
                self.player_stats['achievements'].append(achievement)
    
    def view_player_statistics(self):
        """Display comprehensive player statistics."""
        print("\n📊 PLAYER STATISTICS")
        print("=" * 40)
        
        stats = self.player_stats
        
        print(f"Games Played: {stats['games_played']}")
        print(f"Total Score: {stats['total_score']:,}")
        print(f"Average Score: {stats['total_score'] / max(1, stats['games_played']):.1f}")
        print(f"Total Enemies Defeated: {stats['total_enemies_defeated']}")
        print(f"Best Survival Time: {stats['best_survival_time']}s")
        print()
        
        print("🏆 HIGH SCORES BY GAME:")
        for game_type, score in self.high_scores.items():
            print(f"  {game_type.replace('_', ' ').title()}: {score:,}")
        
        print(f"\n🎖️ ACHIEVEMENTS ({len(stats['achievements'])}):")
        achievement_names = {
            'high_scorer': 'High Scorer - Reach 1,000 points',
            'enemy_hunter': 'Enemy Hunter - Defeat 10 enemies',
            'collector': 'Collector - Collect 20 pickups',
            'survivor': 'Survivor - Survive for 5 minutes'
        }
        
        for achievement in stats['achievements']:
            print(f"  ✅ {achievement_names.get(achievement, achievement)}")
        
        # Show locked achievements
        locked = set(achievement_names.keys()) - set(stats['achievements'])
        if locked:
            print(f"\n🔒 LOCKED ACHIEVEMENTS:")
            for achievement in locked:
                print(f"  ❌ {achievement_names[achievement]}")
        
        input("\nPress Enter to continue...")
    
    def load_game_data(self):
        """Load saved game data."""
        try:
            with open('game_data.json', 'r') as f:
                data = json.load(f)
                self.high_scores = data.get('high_scores', {})
                self.player_stats = data.get('player_stats', self.player_stats)
        except FileNotFoundError:
            pass  # Use default values
        except json.JSONDecodeError:
            print("⚠️ Warning: Could not load game data file")
    
    def save_game_data(self):
        """Save game data to file."""
        try:
            data = {
                'high_scores': self.high_scores,
                'player_stats': self.player_stats,
                'save_date': datetime.now().isoformat()
            }
            
            with open('game_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        
        except Exception as e:
            print(f"⚠️ Warning: Could not save game data: {e}")
    
    def run(self):
        """Main game engine loop."""
        print("🎮 Welcome to the Game Development Engine!")
        print("Create, play, and master multiple game types with advanced AI and physics.")
        
        while True:
            self.display_main_menu()
            choice = self.get_menu_choice()
            
            if choice == 0:
                print("\n🎮 Thanks for playing! Keep developing awesome games!")
                break
            elif 1 <= choice <= len(self.game_types):
                game_type = list(self.game_types.keys())[choice - 1]
                self.play_game(game_type)
            elif choice == len(self.game_types) + 1:
                self.view_player_statistics()
            elif choice == len(self.game_types) + 2:
                print("🚧 Game development tools coming soon!")
                input("Press Enter to continue...")
            elif choice == len(self.game_types) + 3:
                print("🚧 Achievement gallery coming soon!")
                input("Press Enter to continue...")

def main():
    """Main entry point for the program."""
    game_engine = GameEngine()
    game_engine.run()

if __name__ == "__main__":
    main()

"""
SOLUTION REQUIREMENTS:
=====================
Your solution should include:
1. ✅ Advanced object-oriented game engine architecture
2. ✅ Multiple game types with different mechanics and objectives
3. ✅ Sophisticated AI behavior patterns and pathfinding
4. ✅ Physics simulation and collision detection systems
5. ✅ Player progression, scoring, and achievement systems
6. ✅ Real-time game state management and rendering
7. ✅ Professional game development tools and debugging
8. ✅ Save/load functionality and persistent player data

LEARNING OUTCOMES:
==================
After completing this problem, you will have mastered:
• Advanced software architecture and design pattern implementation
• Game development principles including AI, physics, and real-time systems
• Complex algorithm design and optimization for performance
• Professional object-oriented programming with inheritance hierarchies
• State management and event-driven programming concepts
• File I/O and data persistence in real-world applications
• Integration of all programming fundamentals in a complex interactive system
• Advanced debugging and system monitoring techniques

EXTENSION IDEAS:
===============
1. Add networked multiplayer capabilities
2. Implement advanced graphics with sprite animations
3. Create level editor and game development tools
4. Add procedural content generation algorithms
5. Implement advanced AI with machine learning
6. Add sound effects and music integration
7. Create mobile game export capabilities
8. Add VR/AR game support and 3D environments

This expert-level problem demonstrates mastery of ALL course concepts
while creating a professional-grade game development engine!
"""