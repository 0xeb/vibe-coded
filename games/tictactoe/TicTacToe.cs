using System;
using System.Drawing;
using System.Windows.Forms;

namespace TicTacToe
{
    public partial class TicTacToeForm : Form
    {
        // Constants
        private const int SCREEN_SIZE = 600;
        private const int CELL_SIZE = SCREEN_SIZE / 3;
        private readonly Color BACKGROUND_COLOR = Color.White;
        private readonly Color LINE_COLOR = Color.Black;
        private readonly Color X_COLOR = Color.Blue;
        private readonly Color O_COLOR = Color.Red;
        private const int LINE_WIDTH = 2;
        private const int SYMBOL_WIDTH = 3;
        private const int SYMBOL_MARGIN = 50;
        private const int FONT_SIZE = 20;

        private Board gameBoard;
        private Label statusLabel;

        public TicTacToeForm()
        {
            InitializeComponents();
            gameBoard = new Board();
        }

        private void InitializeComponents()
        {
            this.Text = "Tic Tac Toe";
            this.Size = new Size(SCREEN_SIZE, SCREEN_SIZE + 60); // Extra height for status label
            this.BackColor = BACKGROUND_COLOR;
            this.DoubleBuffered = true;
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.StartPosition = FormStartPosition.CenterScreen;

            // Add status label at the bottom
            statusLabel = new Label
            {
                TextAlign = ContentAlignment.MiddleCenter,
                Width = SCREEN_SIZE,
                Height = 30,
                Location = new Point(0, SCREEN_SIZE),
                Font = new Font("Arial", FONT_SIZE)
            };
            this.Controls.Add(statusLabel);

            // Add event handlers
            this.Paint += TicTacToeForm_Paint;
            this.MouseClick += TicTacToeForm_MouseClick;
            this.KeyDown += TicTacToeForm_KeyDown;

            // Set the initial status text
            UpdateStatus();
        }

        private void TicTacToeForm_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            DrawGrid(g);
            DrawSymbols(g);
        }

        private void TicTacToeForm_MouseClick(object sender, MouseEventArgs e)
        {
            if (gameBoard.GameOver)
                return;

            Tuple<int, int> cell = GetCellFromPosition(e.X, e.Y);
            if (cell != null)
            {
                int row = cell.Item1;
                int col = cell.Item2;
                if (gameBoard.MakeMove(row, col))
                {
                    UpdateStatus();
                    this.Invalidate(); // Force redraw
                }
            }
        }

        private void TicTacToeForm_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.R)
            {
                gameBoard.ResetGame();
                UpdateStatus();
                this.Invalidate();
            }
        }

        private Tuple<int, int> GetCellFromPosition(int x, int y)
        {
            if (x < 0 || x >= SCREEN_SIZE || y < 0 || y >= SCREEN_SIZE)
                return null;

            int row = y / CELL_SIZE;
            int col = x / CELL_SIZE;
            if (row >= 0 && row < 3 && col >= 0 && col < 3)
                return new Tuple<int, int>(row, col);

            return null;
        }

        private void DrawGrid(Graphics g)
        {
            using (Pen pen = new Pen(LINE_COLOR, LINE_WIDTH))
            {
                // Draw vertical lines
                for (int x = CELL_SIZE; x < SCREEN_SIZE; x += CELL_SIZE)
                {
                    g.DrawLine(pen, x, 0, x, SCREEN_SIZE);
                }

                // Draw horizontal lines
                for (int y = CELL_SIZE; y < SCREEN_SIZE; y += CELL_SIZE)
                {
                    g.DrawLine(pen, 0, y, SCREEN_SIZE, y);
                }
            }
        }

        private void DrawSymbols(Graphics g)
        {
            for (int row = 0; row < 3; row++)
            {
                for (int col = 0; col < 3; col++)
                {
                    int centerX = col * CELL_SIZE + CELL_SIZE / 2;
                    int centerY = row * CELL_SIZE + CELL_SIZE / 2;

                    if (gameBoard.Grid[row, col] == 'X')
                    {
                        // Draw X
                        using (Pen pen = new Pen(X_COLOR, SYMBOL_WIDTH))
                        {
                            int startX = centerX - CELL_SIZE / 2 + SYMBOL_MARGIN;
                            int endX = centerX + CELL_SIZE / 2 - SYMBOL_MARGIN;
                            int startY = centerY - CELL_SIZE / 2 + SYMBOL_MARGIN;
                            int endY = centerY + CELL_SIZE / 2 - SYMBOL_MARGIN;
                            g.DrawLine(pen, startX, startY, endX, endY);
                            g.DrawLine(pen, startX, endY, endX, startY);
                        }
                    }
                    else if (gameBoard.Grid[row, col] == 'O')
                    {
                        // Draw O
                        using (Pen pen = new Pen(O_COLOR, SYMBOL_WIDTH))
                        {
                            int radius = CELL_SIZE / 2 - SYMBOL_MARGIN;
                            g.DrawEllipse(pen, centerX - radius, centerY - radius, radius * 2, radius * 2);
                        }
                    }
                }
            }
        }

        private void UpdateStatus()
        {
            if (gameBoard.GameOver)
            {
                if (gameBoard.Winner != '\0')
                {
                    statusLabel.Text = $"Player {gameBoard.Winner} wins! Press R to restart";
                }
                else
                {
                    statusLabel.Text = "It's a draw! Press R to restart";
                }
            }
            else
            {
                statusLabel.Text = $"Player {gameBoard.CurrentPlayer}'s turn";
            }
        }
    }

    public class Board
    {
        public char[,] Grid { get; private set; }
        public char CurrentPlayer { get; private set; }
        public char Winner { get; private set; }
        public bool GameOver { get; private set; }

        public Board()
        {
            ResetGame();
        }

        public void ResetGame()
        {
            // Initialize empty 3x3 board
            Grid = new char[3, 3];
            for (int row = 0; row < 3; row++)
            {
                for (int col = 0; col < 3; col++)
                {
                    Grid[row, col] = '\0';
                }
            }
            CurrentPlayer = 'X';
            Winner = '\0';
            GameOver = false;
        }

        public bool IsValidMove(int row, int col)
        {
            return Grid[row, col] == '\0' && !GameOver;
        }

        public bool MakeMove(int row, int col)
        {
            if (IsValidMove(row, col))
            {
                Grid[row, col] = CurrentPlayer;
                if (CheckWinner(row, col))
                {
                    Winner = CurrentPlayer;
                    GameOver = true;
                }
                else if (IsBoardFull())
                {
                    GameOver = true;
                }
                else
                {
                    CurrentPlayer = CurrentPlayer == 'X' ? 'O' : 'X';
                }
                return true;
            }
            return false;
        }

        private bool CheckWinner(int row, int col)
        {
            // Check row
            bool rowWin = true;
            for (int c = 0; c < 3; c++)
            {
                if (Grid[row, c] != CurrentPlayer)
                {
                    rowWin = false;
                    break;
                }
            }
            if (rowWin) return true;

            // Check column
            bool colWin = true;
            for (int r = 0; r < 3; r++)
            {
                if (Grid[r, col] != CurrentPlayer)
                {
                    colWin = false;
                    break;
                }
            }
            if (colWin) return true;

            // Check diagonals
            if (row == col)
            {
                bool diagWin = true;
                for (int i = 0; i < 3; i++)
                {
                    if (Grid[i, i] != CurrentPlayer)
                    {
                        diagWin = false;
                        break;
                    }
                }
                if (diagWin) return true;
            }

            if (row + col == 2)
            {
                bool antiDiagWin = true;
                for (int i = 0; i < 3; i++)
                {
                    if (Grid[i, 2 - i] != CurrentPlayer)
                    {
                        antiDiagWin = false;
                        break;
                    }
                }
                if (antiDiagWin) return true;
            }

            return false;
        }

        private bool IsBoardFull()
        {
            for (int row = 0; row < 3; row++)
            {
                for (int col = 0; col < 3; col++)
                {
                    if (Grid[row, col] == '\0')
                    {
                        return false;
                    }
                }
            }
            return true;
        }
    }

    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new TicTacToeForm());
        }
    }
}
