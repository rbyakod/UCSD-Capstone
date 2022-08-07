mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"rbyakod@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = 8081\n\
" > ~/.streamlit/config.toml
