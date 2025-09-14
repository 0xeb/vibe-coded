// Game Constants (matching Python version)
const WINDOW_WIDTH = 400;
const WINDOW_HEIGHT = 600;
const GROUND_HEIGHT = 100;

// Bird physics
const BIRD_WIDTH = 40;
const BIRD_HEIGHT = 30;
const BIRD_X = 50;
const GRAVITY = 0.38;
const JUMP_STRENGTH = -7;
const JUMP_HOLD_BOOST = -0.35;
const JUMP_HOLD_FRAMES = 14;

// Pipe settings
const PIPE_WIDTH = 80;
const PIPE_GAP = 190;
const PIPE_SPEED = 3;
const PIPE_INTERVAL = 2200;

// Cloud settings
const CLOUD_COUNT = 6;
const CLOUD_MIN_SPEED = 0.3;
const CLOUD_MAX_SPEED = 0.9;
const CLOUD_MIN_SCALE = 0.6;
const CLOUD_MAX_SCALE = 1.3;

// Colors
const BG_COLOR = 0x87CEFA; // Light blue
const GROUND_COLOR = 0x8B4513; // Brown
const BIRD_COLOR = 0xFFD700; // Yellow
const PIPE_BODY_COLOR = 0x228B22; // Green
const PIPE_CAP_COLOR = 0xC0C0C0; // Silver
const CLOUD_COLOR = 0xFFFFFF; // White

// Game states
const STATE_START = 0;
const STATE_PLAYING = 1;
const STATE_GAMEOVER = 2;
const STATE_PAUSED = 3;

class StartScene extends Phaser.Scene {
    constructor() {
        super({ key: 'StartScene' });
    }

    create() {
        this.cameras.main.setBackgroundColor(BG_COLOR);
        
        // Clouds in background
        this.clouds = [];
        for (let i = 0; i < CLOUD_COUNT; i++) {
            this.createCloud();
        }

        // Title text
        const titleText = this.add.text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3, 'Flappy Bird', {
            fontSize: '36px',
            fontStyle: 'bold',
            color: '#ffffff'
        });
        titleText.setOrigin(0.5);

        // Start instruction
        const startText = this.add.text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 'Press SPACE to start', {
            fontSize: '24px',
            color: '#ffffff'
        });
        startText.setOrigin(0.5);

        // Input handling
        this.input.keyboard.on('keydown-SPACE', () => {
            this.scene.start('PlayScene');
        });
    }

    update() {
        // Update clouds
        this.clouds.forEach((cloud, index) => {
            cloud.x -= cloud.speed;
            if (cloud.x + cloud.width < 0) {
                cloud.x = WINDOW_WIDTH + Phaser.Math.Between(0, 120);
                cloud.y = Phaser.Math.Between(10, WINDOW_HEIGHT - GROUND_HEIGHT - 200);
            }
        });
    }

    createCloud() {
        const scale = Phaser.Math.FloatBetween(CLOUD_MIN_SCALE, CLOUD_MAX_SCALE);
        const width = 100 * scale;
        const height = 60 * scale;
        const x = Phaser.Math.Between(0, WINDOW_WIDTH);
        const y = Phaser.Math.Between(10, WINDOW_HEIGHT - GROUND_HEIGHT - 200);
        
        const cloud = this.add.graphics();
        cloud.fillStyle(CLOUD_COLOR, 0.8);
        
        // Draw cloud shape with multiple ellipses
        cloud.fillEllipse(width * 0.25, height * 0.35, width * 0.42, height * 0.5);
        cloud.fillEllipse(width * 0.5, height * 0.45, width * 0.5, height * 0.6);
        cloud.fillEllipse(width * 0.75, height * 0.5, width * 0.45, height * 0.5);
        cloud.fillEllipse(width * 0.6, height * 0.35, width * 0.4, height * 0.55);
        
        cloud.x = x;
        cloud.y = y;
        cloud.width = width;
        cloud.height = height;
        cloud.speed = Phaser.Math.FloatBetween(CLOUD_MIN_SPEED, CLOUD_MAX_SPEED);
        
        this.clouds.push(cloud);
    }
}

class PlayScene extends Phaser.Scene {
    constructor() {
        super({ key: 'PlayScene' });
    }

    create() {
        this.cameras.main.setBackgroundColor(BG_COLOR);
        
        // Game variables
        this.score = 0;
        this.lives = 3;
        this.gameState = STATE_PLAYING;
        this.collisionCooldown = 0;
        this.impactTimer = 0;
        this.impactPos = null;
        this.godMode = false;
        this.isPaused = false;
        
        // Clouds
        this.clouds = [];
        for (let i = 0; i < CLOUD_COUNT; i++) {
            this.createCloud();
        }
        
        // Ground
        this.ground = this.add.rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT - GROUND_HEIGHT / 2, 
                                         WINDOW_WIDTH, GROUND_HEIGHT, GROUND_COLOR);
        
        // Bird
        this.bird = this.createBird();
        
        // Pipes group
        this.pipes = [];
        this.lastPipeTime = 0;
        
        // Score text
        this.scoreText = this.add.text(WINDOW_WIDTH / 2, 50, '0', {
            fontSize: '36px',
            fontStyle: 'bold',
            color: '#ffffff'
        });
        this.scoreText.setOrigin(0.5);
        this.scoreText.setDepth(10);
        
        // Lives text
        this.livesText = this.add.text(10, 10, 'Lives: 3', {
            fontSize: '24px',
            color: '#ffffff'
        });
        this.livesText.setDepth(10);
        
        // God mode text (hidden initially)
        this.godText = this.add.text(WINDOW_WIDTH - 10, 10, 'GOD', {
            fontSize: '24px',
            color: '#FFD700'
        });
        this.godText.setOrigin(1, 0);
        this.godText.setVisible(false);
        this.godText.setDepth(10);
        
        // Pause overlay (hidden initially)
        this.pauseOverlay = this.add.group([
            this.add.rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT, 0x000000, 0.5),
            this.add.text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 20, 'Paused', {
                fontSize: '36px',
                fontStyle: 'bold',
                color: '#ffffff'
            }).setOrigin(0.5),
            this.add.text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 30, 'Press P to resume', {
                fontSize: '24px',
                color: '#ffffff'
            }).setOrigin(0.5)
        ]);
        this.pauseOverlay.setVisible(false);
        this.pauseOverlay.children.entries.forEach(child => child.setDepth(20));
        
        // Input handling
        this.setupInput();
    }

    createBird() {
        const bird = this.add.graphics();
        bird.x = BIRD_X;
        bird.y = WINDOW_HEIGHT / 2 - BIRD_HEIGHT / 2;
        bird.velocity = 0;
        bird.jumpHeld = false;
        bird.jumpBoostFrames = 0;
        
        // Draw bird
        bird.draw = () => {
            bird.clear();
            // Body
            bird.fillStyle(0xFFFF00);
            bird.fillEllipse(20, 15, 40, 30);
            // Wing
            bird.fillStyle(0xFFA500);
            bird.fillEllipse(20, 15, 20, 10);
            // Beak
            bird.fillStyle(0xFFA500);
            bird.fillTriangle(40, 15, 50, 20, 40, 20);
            // Eye
            bird.fillStyle(0x000000);
            bird.fillCircle(30, 10, 3);
        };
        
        bird.draw();
        bird.setDepth(5);
        
        // Collision bounds
        bird.bounds = () => {
            return {
                x: bird.x,
                y: bird.y,
                width: BIRD_WIDTH,
                height: BIRD_HEIGHT,
                right: bird.x + BIRD_WIDTH,
                bottom: bird.y + BIRD_HEIGHT
            };
        };
        
        return bird;
    }

    createCloud() {
        const scale = Phaser.Math.FloatBetween(CLOUD_MIN_SCALE, CLOUD_MAX_SCALE);
        const width = 100 * scale;
        const height = 60 * scale;
        const x = Phaser.Math.Between(0, WINDOW_WIDTH);
        const y = Phaser.Math.Between(10, WINDOW_HEIGHT - GROUND_HEIGHT - 200);
        
        const cloud = this.add.graphics();
        cloud.fillStyle(CLOUD_COLOR, 0.8);
        
        // Draw cloud shape
        cloud.fillEllipse(width * 0.25, height * 0.35, width * 0.42, height * 0.5);
        cloud.fillEllipse(width * 0.5, height * 0.45, width * 0.5, height * 0.6);
        cloud.fillEllipse(width * 0.75, height * 0.5, width * 0.45, height * 0.5);
        cloud.fillEllipse(width * 0.6, height * 0.35, width * 0.4, height * 0.55);
        
        cloud.x = x;
        cloud.y = y;
        cloud.width = width;
        cloud.height = height;
        cloud.speed = Phaser.Math.FloatBetween(CLOUD_MIN_SPEED, CLOUD_MAX_SPEED);
        cloud.setDepth(0);
        
        this.clouds.push(cloud);
    }

    createPipe() {
        const gapY = Phaser.Math.Between(80, WINDOW_HEIGHT - GROUND_HEIGHT - 80 - PIPE_GAP);
        
        const pipeGroup = this.add.group();
        
        // Top pipe
        const topPipe = this.add.graphics();
        topPipe.x = WINDOW_WIDTH;
        topPipe.y = 0;
        topPipe.height = gapY;
        
        // Draw top pipe
        topPipe.fillStyle(PIPE_BODY_COLOR);
        topPipe.fillRect(0, 0, PIPE_WIDTH, gapY);
        // Cap
        topPipe.fillStyle(PIPE_CAP_COLOR);
        topPipe.fillRect(-6, gapY - 20, PIPE_WIDTH + 12, 20);
        // Shading
        topPipe.fillStyle(0x145A14);
        topPipe.fillRect(4, 0, 6, gapY);
        topPipe.fillStyle(0x3CAA3C);
        topPipe.fillRect(PIPE_WIDTH - 10, 0, 6, gapY);
        
        topPipe.setDepth(3);
        
        // Bottom pipe
        const bottomPipe = this.add.graphics();
        bottomPipe.x = WINDOW_WIDTH;
        bottomPipe.y = gapY + PIPE_GAP;
        bottomPipe.height = WINDOW_HEIGHT - GROUND_HEIGHT - (gapY + PIPE_GAP);
        
        // Draw bottom pipe
        bottomPipe.fillStyle(PIPE_BODY_COLOR);
        bottomPipe.fillRect(0, 0, PIPE_WIDTH, bottomPipe.height);
        // Cap
        bottomPipe.fillStyle(PIPE_CAP_COLOR);
        bottomPipe.fillRect(-6, 0, PIPE_WIDTH + 12, 20);
        // Shading
        bottomPipe.fillStyle(0x145A14);
        bottomPipe.fillRect(4, 0, 6, bottomPipe.height);
        bottomPipe.fillStyle(0x3CAA3C);
        bottomPipe.fillRect(PIPE_WIDTH - 10, 0, 6, bottomPipe.height);
        
        bottomPipe.setDepth(3);
        
        pipeGroup.add(topPipe);
        pipeGroup.add(bottomPipe);
        pipeGroup.passed = false;
        pipeGroup.topPipe = topPipe;
        pipeGroup.bottomPipe = bottomPipe;
        
        this.pipes.push(pipeGroup);
    }

    setupInput() {
        const keyboard = this.input.keyboard;
        
        // Jump controls
        keyboard.on('keydown-SPACE', () => {
            if (this.gameState === STATE_PLAYING && !this.isPaused) {
                this.birdJump();
            }
        });
        
        keyboard.on('keyup-SPACE', () => {
            if (this.gameState === STATE_PLAYING && !this.isPaused) {
                this.birdJumpRelease();
            }
        });
        
        // Mouse/touch controls
        this.input.on('pointerdown', () => {
            if (this.gameState === STATE_PLAYING && !this.isPaused) {
                this.birdJump();
            }
        });
        
        this.input.on('pointerup', () => {
            if (this.gameState === STATE_PLAYING && !this.isPaused) {
                this.birdJumpRelease();
            }
        });
        
        // Debug controls
        keyboard.on('keydown-I', () => {
            if (this.gameState === STATE_PLAYING) {
                this.lives += 5;
                this.livesText.setText('Lives: ' + this.lives);
            }
        });
        
        keyboard.on('keydown-G', () => {
            this.godMode = !this.godMode;
            this.godText.setVisible(this.godMode);
        });
        
        // Pause control
        keyboard.on('keydown-P', () => {
            if (this.gameState === STATE_PLAYING) {
                this.isPaused = !this.isPaused;
                this.pauseOverlay.setVisible(this.isPaused);
            }
        });
        
        // Escape to menu
        keyboard.on('keydown-ESC', () => {
            this.scene.start('StartScene');
        });
    }

    birdJump() {
        this.bird.velocity = JUMP_STRENGTH;
        this.bird.jumpBoostFrames = JUMP_HOLD_FRAMES;
        this.bird.jumpHeld = true;
    }

    birdJumpRelease() {
        this.bird.jumpHeld = false;
        this.bird.jumpBoostFrames = 0;
    }

    update(time, delta) {
        if (this.gameState !== STATE_PLAYING || this.isPaused) {
            // Only update clouds when paused or in other states
            if (this.gameState === STATE_START || !this.isPaused) {
                this.updateClouds();
            }
            return;
        }

        // Update clouds
        this.updateClouds();

        // Update bird physics
        if (this.bird.jumpHeld && this.bird.jumpBoostFrames > 0) {
            this.bird.velocity += JUMP_HOLD_BOOST;
            this.bird.jumpBoostFrames--;
        }
        this.bird.velocity += GRAVITY;
        this.bird.y += this.bird.velocity;
        this.bird.draw();

        // Spawn pipes
        if (time - this.lastPipeTime > PIPE_INTERVAL) {
            this.createPipe();
            this.lastPipeTime = time;
        }

        // Update pipes
        this.pipes = this.pipes.filter(pipeGroup => {
            pipeGroup.topPipe.x -= PIPE_SPEED;
            pipeGroup.bottomPipe.x -= PIPE_SPEED;
            
            // Check if passed for scoring
            if (!pipeGroup.passed && pipeGroup.topPipe.x + PIPE_WIDTH < this.bird.x) {
                this.score++;
                this.scoreText.setText(this.score.toString());
                pipeGroup.passed = true;
            }
            
            // Remove off-screen pipes
            if (pipeGroup.topPipe.x + PIPE_WIDTH < 0) {
                pipeGroup.destroy(true);
                return false;
            }
            return true;
        });

        // Collision detection
        if (this.collisionCooldown === 0) {
            let hit = false;
            let impactX = 0, impactY = 0;

            // Check pipe collisions
            const birdBounds = this.bird.bounds();
            this.pipes.forEach(pipeGroup => {
                const topPipe = pipeGroup.topPipe;
                const bottomPipe = pipeGroup.bottomPipe;
                
                // Top pipe collision
                if (birdBounds.x < topPipe.x + PIPE_WIDTH && 
                    birdBounds.right > topPipe.x &&
                    birdBounds.y < topPipe.height) {
                    hit = true;
                    impactX = birdBounds.x + BIRD_WIDTH / 2;
                    impactY = topPipe.height;
                }
                
                // Bottom pipe collision
                if (birdBounds.x < bottomPipe.x + PIPE_WIDTH && 
                    birdBounds.right > bottomPipe.x &&
                    birdBounds.bottom > bottomPipe.y) {
                    hit = true;
                    impactX = birdBounds.x + BIRD_WIDTH / 2;
                    impactY = bottomPipe.y;
                }
            });

            // Ground collision
            if (birdBounds.bottom > WINDOW_HEIGHT - GROUND_HEIGHT) {
                hit = true;
                impactX = birdBounds.x + BIRD_WIDTH / 2;
                impactY = WINDOW_HEIGHT - GROUND_HEIGHT;
            }

            // Ceiling collision
            if (birdBounds.y < 0) {
                hit = true;
                impactX = birdBounds.x + BIRD_WIDTH / 2;
                impactY = 0;
            }

            if (hit) {
                if (!this.godMode) {
                    this.lives--;
                    this.livesText.setText('Lives: ' + this.lives);
                    this.collisionCooldown = 60; // 1 second at 60 FPS
                    this.impactTimer = 36; // 0.6 seconds
                    
                    if (this.lives <= 0) {
                        this.gameState = STATE_GAMEOVER;
                        this.scene.start('GameOverScene', { score: this.score });
                    } else {
                        // Reset bird position
                        this.bird.y = WINDOW_HEIGHT / 2 - BIRD_HEIGHT / 2;
                        this.bird.velocity = 0;
                    }
                } else {
                    this.impactTimer = 18; // Brief flash in god mode
                }
                
                this.impactPos = { x: impactX, y: impactY };
            }
        } else {
            this.collisionCooldown = Math.max(0, this.collisionCooldown - 1);
        }

        // Update impact timer and draw cross
        if (this.impactTimer > 0) {
            this.impactTimer--;
            
            // Flash every 6 frames
            if (Math.floor(this.impactTimer / 6) % 2 === 0 && this.impactPos) {
                this.drawImpactCross(this.impactPos.x, this.impactPos.y);
            }
            
            if (this.impactTimer === 0) {
                this.impactPos = null;
            }
        }
    }

    updateClouds() {
        this.clouds.forEach(cloud => {
            cloud.x -= cloud.speed;
            if (cloud.x + cloud.width < 0) {
                cloud.x = WINDOW_WIDTH + Phaser.Math.Between(0, 120);
                cloud.y = Phaser.Math.Between(10, WINDOW_HEIGHT - GROUND_HEIGHT - 200);
            }
        });
    }

    drawImpactCross(x, y) {
        const cross = this.add.graphics();
        cross.lineStyle(3, 0xFF0000);
        const size = 13;
        cross.moveTo(x - size, y - size);
        cross.lineTo(x + size, y + size);
        cross.moveTo(x - size, y + size);
        cross.lineTo(x + size, y - size);
        cross.strokePath();
        cross.setDepth(15);
        
        // Remove after one frame
        this.time.delayedCall(16, () => cross.destroy());
    }
}

class GameOverScene extends Phaser.Scene {
    constructor() {
        super({ key: 'GameOverScene' });
    }

    init(data) {
        this.finalScore = data.score || 0;
    }

    create() {
        this.cameras.main.setBackgroundColor(BG_COLOR);
        
        // Game Over text
        const gameOverText = this.add.text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3, 'Game Over', {
            fontSize: '36px',
            fontStyle: 'bold',
            color: '#ffffff'
        });
        gameOverText.setOrigin(0.5);

        // Score text
        const scoreText = this.add.text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 'Score: ' + this.finalScore, {
            fontSize: '24px',
            color: '#ffffff'
        });
        scoreText.setOrigin(0.5);

        // Restart instruction
        const restartText = this.add.text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 40, 'Press SPACE to restart', {
            fontSize: '24px',
            color: '#ffffff'
        });
        restartText.setOrigin(0.5);

        // Input handling
        this.input.keyboard.on('keydown-SPACE', () => {
            this.scene.start('StartScene');
        });
    }
}

// Game configuration
const config = {
    type: Phaser.AUTO,
    width: WINDOW_WIDTH,
    height: WINDOW_HEIGHT,
    parent: 'game-container',
    scene: [StartScene, PlayScene, GameOverScene],
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 },
            debug: false
        }
    }
};

// Create game
const game = new Phaser.Game(config);