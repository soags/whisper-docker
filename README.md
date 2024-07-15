# Whisper Docker

Dockerコンテナ上でOpenAI Whisperを実行し、音声ファイルの文字起こしを行います。

## 実行環境

- Docker Desktop

## 使い方

1. プロジェクトの`/audio`に音声ファイルを配置する。

1. docker-composeを実行する。

```
docker compose up --build
```

1. `/text`にテキストファイルが出力されます。

## トラブルシューティング

### テキストファイルが作成されない

コンソールに以下のログが出力されている場合、メモリが足りていません。

```
exited with code 137
```