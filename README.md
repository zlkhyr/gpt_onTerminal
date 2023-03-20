# Berinteraksi dengan GPT di terminal 

Ini adalah code Python yang memungkinkan anda berinteraksi dengan API ChatGPT untuk menghasilkan respons berdasarkan input pengguna.

## Setting Up

Sebelum menjalankan code, pastikan Anda telah menginstal dependensi yang diperlukan, yaitu : `openai`.

```sh
pip install openai
```

Anda juga memerlukan OpenAI API key untuk menggunakan API. Setelah Anda memiliki kunci API, ekspor sebagai environment variable  di terminal Anda menggunakan perintah berikut:

```sh
export OPENAI_API_KEY="sk-XXXX"
```

## Membuat Shortcut di terminal

Buat file gpt.py dapat dieksekusi menggunakan perintah berikut:

```sh
chmod +x gpt.py
```

Selanjutnya, Buat sebuah alias di shell configuration file (e.g. ~/.bashrc or ~/.zshrc) dengan menggunakan command berikut:

```sh
alias gpt="/path/to/gpt.py"
```

ganti "/path/to" dengan path ke directory yang punya file gpt.py 

## References
- [Pixegami](https://github.com/pixegami/gpt-shell)
- [OpenAI API documentation](https://platform.openai.com/docs/guides/chat)
- [Python argparse tutorial](https://docs.python.org/3/howto/argparse.html)
