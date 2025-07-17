# Enhanced Q&A Chatbot with Ollama

A powerful, web-based question-and-answer chatbot application built with Streamlit and powered by various open-source language models through Ollama integration. This application provides an intuitive interface for interacting with multiple LLMs with configurable parameters for customized responses.

## Features

- **Multiple Model Support**: Choose from 9 different open-source language models including Gemma, Mistral, LLaMA, and specialized models
- **Interactive Web Interface**: Clean, responsive Streamlit-based UI for seamless user experience
- **Configurable Parameters**: Adjust temperature and max tokens to fine-tune response characteristics
- **Real-time Processing**: Instant response generation with loading indicators
- **Error Handling**: Robust error management with user-friendly messages
- **LangSmith Integration**: Built-in tracing and monitoring for debugging and performance analysis

## Supported Models

| Model | Description | Best For |
|-------|-------------|----------|
| `gemma:2b` | Google's lightweight model | Fast responses, general queries |
| `mistral` | Fast, accurate small model | Balanced performance |
| `llama2:7b` | Meta's LLaMA 2 | General-purpose conversations |
| `llama3:8b` | Enhanced LLaMA version | Advanced reasoning tasks |
| `phi3:mini` | Microsoft's efficient model | Resource-constrained environments |
| `dolphin-mixtral` | Fine-tuned Mistral variant | Conversational AI |
| `openchat:7b` | Chat-optimized model | Interactive dialogues |
| `neural-chat` | Intel's conversational model | General-purpose chat |
| `starcoder2:3b` | Specialized coding model | Programming and code generation |

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- Ollama (for running local language models)
- Git (for cloning the repository)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/enhanced-qa-chatbot.git
cd enhanced-qa-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and Setup Ollama

#### On macOS/Linux:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

#### On Windows:
Download and install from [ollama.ai](https://ollama.ai/download)

### 5. Pull Required Models

```bash
# Pull at least one model (example with Gemma)
ollama pull gemma:2b

# Optional: Pull additional models
ollama pull mistral
ollama pull llama2:7b
```

### 6. Environment Configuration

Create a `.env` file in the project root:

```env
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

**Note**: The LangChain API key is optional but recommended for enhanced tracing and monitoring capabilities.

## Usage

### Starting the Application

1. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

2. Launch the Streamlit application:
   ```bash
   streamlit run app.py
   ```

3. Open your browser and navigate to `http://localhost:8501`

### Using the Interface

1. **Select a Model**: Choose from the dropdown in the sidebar
2. **Configure Parameters**:
   - **Temperature** (0.0-1.0): Controls response creativity
     - 0.0-0.3: Factual, deterministic responses
     - 0.4-0.7: Balanced creativity and accuracy
     - 0.8-1.0: Highly creative, varied responses
   - **Max Tokens** (50-300): Controls response length
3. **Ask Questions**: Type your question in the input field
4. **View Response**: The AI-generated answer will appear below

## Project Structure

```
enhanced-qa-chatbot/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .env.example          # Environment variables template
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
```

## Configuration

### Model Parameters

- **Temperature**: Controls randomness in responses
  - Lower values (0.0-0.3): More focused, deterministic
  - Higher values (0.7-1.0): More creative, varied
- **Max Tokens**: Limits response length (50-300 tokens)

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `LANGCHAIN_API_KEY` | API key for LangSmith tracing | Optional |
| `LANGCHAIN_PROJECT` | Project name for tracing | Auto-set |
| `LANGCHAIN_TRACING_V2` | Enable tracing | Auto-set |

## Troubleshooting

### Common Issues

1. **"Model not found" Error**:
   - Ensure Ollama is running: `ollama serve`
   - Pull the model: `ollama pull model_name`

2. **Connection Error**:
   - Verify Ollama is running on default port (11434)
   - Check firewall settings

3. **Slow Response Times**:
   - Try smaller models (gemma:2b, phi3:mini)
   - Reduce max_tokens parameter
   - Ensure adequate system resources

4. **Memory Issues**:
   - Use smaller models
   - Reduce concurrent usage
   - Monitor system memory usage

### Performance Optimization

- **For Speed**: Use `gemma:2b` or `phi3:mini`
- **For Accuracy**: Use `llama3:8b` or `mistral`
- **For Coding**: Use `starcoder2:3b`
- **For General Use**: Use `llama2:7b` or `openchat:7b`

## Development

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request


**Note**: This application runs language models locally through Ollama, ensuring privacy and data security. No user data is sent to external servers unless LangSmith tracing is enabled.
