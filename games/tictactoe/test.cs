using System;
using System.Drawing;
using System.Windows.Forms;

namespace TicTacToe
{
    public partial class MainForm : Form
    {
        private const int CELL_SIZE = 200;
        private const int GRID_SIZE = 3;
        private const int FORM_SIZE = CELL_SIZE * GRID_SIZE;
        private const int LINE_WIDTH = 2;
        private const int SYMBOL_MARGIN = 50;
        
        private Board board;
        private Label statusLabel;
        
        public MainForm()
        {
            InitializeComponent();
            board = new Board();
        }
        
        private void InitializeComponent()
        {
            this.Text = "Tic Tac Toe";
            this.ClientSize = new Size(FORM_SIZE, FORM_SIZE + 50);
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.StartPosition = FormStartPosition.CenterScreen;
            
            // Status label
            statusLabel = new Label
            {
                Text = "Player X's turn",
                TextAlign = ContentAlignment.MiddleCenter,
                Font = new Font("Arial", 16),
                Location = new Point(0, FORM_SIZE),
                Size = new Size(FORM_SIZE, 50)
            };
            this.Controls.Add(statusLabel);
            
            // Event handlers
            this.Paint += MainForm_Paint;
            this.MouseClick += MainForm_MouseClick;
            this.KeyDown += MainForm_KeyDown;
            this.KeyPreview = true;
        }
        
        private void MainForm_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            g.Clear(Color.White);
            
            DrawGrid(g);
            DrawSymbols(g);
        }
        
        private void DrawGrid(Graphics g)
        {
            Pen linePen = new Pen(Color.Black, LINE_WIDTH);
            
            // Draw vertical lines
            for (int i = 1; i < GRID_SIZE; i++)
            {
                int x = i * CELL_SIZE;
                g.DrawLine(linePen, x, 0, x, FORM_SIZE);
            }
            
            // Draw horizontal lines
            for (int i = 1; i < GRID_SIZE; i++)
            {
                int y = i * CELL_SIZE;
                g.DrawLine(linePen, 0, y, FORM_SIZE, y);
            }
        }
        
        private void DrawSymbols(Graphics g)
        {
            for (int row = 0; row < GRID_SIZE; row++)
            {
                for (int col = 0; col < GRID_SIZE; col++)
                {
                    int centerX = col * CELL_SIZE + CELL_SIZE / 2;
                    int centerY = row * CELL_SIZE + CELL_SIZE / 2;
                    
                    if (board.Grid[row, col] == 'X')
                    {
                        DrawX(g, centerX, centerY);
                    }
                    else if (board.Grid[row, col] == 'O')
                    {
                        DrawO(g, centerX, centerY);
                    }
                }
            }
        }
        
        private void DrawX(Graphics g, int centerX, int centerY)
        {
            Pen xPen = new Pen(Color.Blue, 3);
            int halfSize = CELL_SIZE / 2 - SYMBOL_MARGIN;
            
            g.DrawLine(xPen, centerX - halfSize, centerY - halfSize, 
                            centerX + halfSize, centerY + halfSize);
            g.DrawLine(xPen, centerX - halfSize, centerY + halfSize, 
                            centerX + halfSize, centerY - halfSize);
        }
        
        private void DrawO(Graphics g, int centerX, int centerY)
        {
            Pen oPen = new Pen(Color.Red, 3);
            int radius = CELL_SIZE / 2 - SYMBOL_MARGIN;
            
            g.DrawEllipse(oPen, centerX - radius, centerY - radius, 
                               radius * 2, radius * 2);
        }
        
        private void MainForm_MouseClick(object sender, MouseEventArgs e)
        {
            if (board.GameOver)
                return;
                
            int row = e.Y / CELL_SIZE;
            int col = e.X / CELL_SIZE;
            
            if (row >= 0 && row < GRID_SIZE && col >= 0 && col < GRID_SIZE)
            {
                if (board.MakeMove(row, col))
                {
                    UpdateStatus();
                    Invalidate();
                }
            }
        }
        
        private void MainForm_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.R)
            {
                board.ResetGame();
                UpdateStatus();
                Invalidate();
            }
        }
        
        private void UpdateStatus()
        {
            if (board.GameOver)
            {
                if (board.Winner != '\0')
                {
                    statusLabel.Text = $"Player {board.Winner} wins! Press R to restart";
                }
                else
                {
                    statusLabel.Text = "It's a draw! Press R to restart";
                }
            }
            else
            {
                statusLabel.Text = $"Player {board.CurrentPlayer}'s turn";
            }
        }
    }
    
    public class Board
    {
        private char[,] grid;
        private char currentPlayer;
        private char winner;
        private bool gameOver;
        
        public char[,] Grid => grid;
        public char CurrentPlayer => currentPlayer;
        public char Winner => winner;
        public bool GameOver => gameOver;
        
        public Board()
        {
            ResetGame();
        }
        
        public void ResetGame()
        {
            grid = new char[3, 3];
            currentPlayer = 'X';
            winner = '\0';
            gameOver = false;
        }
        
        public bool IsValidMove(int row, int col)
        {
            return grid[row, col] == '\0' && !gameOver;
        }
        
        public bool MakeMove(int row, int col)
        {
            if (IsValidMove(row, col))
            {
                grid[row, col] = currentPlayer;
                
                if (CheckWinner(row, col))
                {
                    winner = currentPlayer;
                    gameOver = true;
                }
                else if (IsBoardFull())
                {
                    gameOver = true;
                }
                else
                {
                    currentPlayer = currentPlayer == 'X' ? 'O' : 'X';
                }
                return true;
            }
            return false;
        }
        
        private bool CheckWinner(int row, int col)
        {
            // Check row
            if (grid[row, 0] == currentPlayer && 
                grid[row, 1] == currentPlayer && 
                grid[row, 2] == currentPlayer)
                return true;
                
            // Check column
            if (grid[0, col] == currentPlayer && 
                grid[1, col] == currentPlayer && 
                grid[2, col] == currentPlayer)
                return true;
                
            // Check diagonal (top-left to bottom-right)
            if (row == col)
            {
                if (grid[0, 0] == currentPlayer && 
                    grid[1, 1] == currentPlayer && 
                    grid[2, 2] == currentPlayer)
                    return true;
            }
            
            // Check diagonal (top-right to bottom-left)
            if (row + col == 2)
            {
                if (grid[0, 2] == currentPlayer && 
                    grid[1, 1] == currentPlayer && 
                    grid[2, 0] == currentPlayer)
                    return true;
            }
            
            return false;
        }
        
        private bool IsBoardFull()
        {
            for (int row = 0; row < 3; row++)
            {
                for (int col = 0; col < 3; col++)
                {
                    if (grid[row, col] == '\0')
                        return false;
                }
            }
            return true;
        }
    }
    
    class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}