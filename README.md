# LineScout

A powerful command-line tool for analyzing codebases by scanning directories, counting files and lines by extension, and generating comprehensive reports with human-readable file sizes and colored output.

## ✨ Features

- **File Analysis**: Count files and lines for specific extensions in any directory
- **Flexible Reporting**: Generate summary reports or detailed comprehensive reports
- **Smart File Detection**: Automatically detects text and binary files
- **Human-Readable Output**: File sizes displayed in KB, MB, GB format
- **Colored Terminal Output**: Visual feedback with colored success and error messages
- **Tabular Format**: Clean, organized table output for easy reading
- **Multiple Report Types**: Choose between extension-specific or full codebase analysis

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/eddo4life/linescout.git
cd linescout
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Syntax
```bash
python main.py [directory] [extension] [options]
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `directory` | Optional | Current directory | Target directory to scan |
| `extension` | Optional | `.txt` | File extension to filter by |

### Options

| Flag | Description |
|------|-------------|
| `--size` | Include file sizes in the summary output |
| `--report` | Generate a detailed report for the specified extension |
| `--full-report` | Generate a comprehensive report covering all file types |

## 💡 Examples

### Basic File Counting
Count Python files in the current directory:
```bash
python main.py . .py
```

### Extension-Specific Report
Generate a detailed report for Markdown files in the `docs` directory:
```bash
python main.py docs .md --report
```

### Comprehensive Analysis
Generate a full report for all file types in the current directory:
```bash
python main.py --full-report
```

### Include File Sizes
Count JavaScript files with size information:
```bash
python main.py src .js --size
```

## 📊 Sample Output

### Full Report Example
```bash
$ python main.py node_modules .md --full-report

Scanning directories : 6it [00:00, 5732.53it/s]
The number of files with extension '.md' is: 1
The total number of lines in those files is: 57

[FULL REPORT]
Analyzing directories : 6it [00:00, 71.07it/s]

File Extension Summary:
Extension      Count  Total Size
-----------  -------  ------------
.json              2  905B
.md                1  1.56KB
.yml               1  480B
.js                3  5.60KB

Text-Based File Details:
name         path                                               lines    size
-----------  -----------------------------------------------  -------  ------
README.md    node_modules\tqdm\README.md                           57    1602
node.js.yml  node_modules\tqdm\.github\workflows\node.js.yml       21     480
index.js     node_modules\tqdm\src\index.js                       145    3245
test.js      node_modules\tqdm\test\test.js                        52    1692
utils.js     node_modules\tqdm\test\utils.js                       41     800
```

## 🛠️ Technical Details

### File Detection
- **Text Files**: Automatically detected and analyzed for line counts
- **Binary Files**: Identified and excluded from line counting
- **File Size Calculation**: Accurate size reporting in human-readable format

### Performance
- Progress bars for directory scanning operations
- Efficient file system traversal
- Optimized for large codebases

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues

If you encounter any problems or have suggestions for improvements, please [open an issue](https://github.com/eddo4life/linescout/issues) on GitHub.

## 📈 Roadmap

- [ ] Support for configuration files
- [ ] Export reports to JSON/CSV formats
- [ ] Integration with popular code editors
- [ ] Performance optimizations for very large repositories
- [ ] Additional file analysis metrics

---

**Made with ❤️ for developers who love clean code analysis**
