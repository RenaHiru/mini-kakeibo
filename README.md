# 🧾 mini-kakeibo

シンプルな家計簿アプリです。  
FastAPI + PostgreSQL + Docker を用いて、**「記録の追加 → 一覧表示」**までの最小機能を実装しています。  
学習とポートフォリオを兼ねたプロジェクトです。

---

## 🚀 概要
- 収支を登録し、一覧で確認できるシンプルな家計簿
- Dockerで環境を統一し、誰でも再現可能
- pytestによる自動テストを導入

---

## 🛠 技術スタック
- **Backend**: Python, FastAPI, SQLAlchemy
- **Database**: PostgreSQL (Dockerコンテナ)
- **Infra**: Docker, Docker Compose
- **Test**: pytest, GitHub Actions (予定)

---

## 💡 私の挑戦と学び
- ブートキャンプ時代は「とにかく動かす」ことを優先してしまい、理解が追いつかず辛い経験をしました  
- このプロジェクトでは **「小さく理解しながら完成させる」** ことを意識し直しました  
- 特に以下に挑戦しました：
  - エラー処理を **try/except** + **logging** で仕込む  
  - DockerでPostgresを立ち上げ、環境依存をなくす  
  - pytestで **正常系テスト** を導入、異常系も追加予定  

👉 失敗を糧にし、巻き返しの一歩として作成したアプリです。

---

## 📂 ディレクトリ構成
```
mini-kakeibo/
├── app/ # FastAPIエンドポイント
├── src/ # アプリの主要ロジック
├── tests/ # pytestテスト
└── docker/ # Docker関連ファイル
```
## ⚡ 使い方
1. リポジトリをクローン
```bash
git clone https://github.com/RenaHiru/mini-kakeibo.git
cd mini-kakeibo
```

2. `.env.example` をコピーして `.env` を作成

3. Dockerで起動
```bash
docker compose up --build -d
```

4. ブラウザで [http://localhost:8000/docs](http://localhost:8000/docs)を開く

## 💡 工夫点

- エラー処理に try/except と logging を導入
- Docker + Postgresで 環境依存を解消
- 最小限の機能に絞って 「まず完成させる」 を優先
- pytestで 正常系テスト を導入済み、異常系も追加予定


## 🚧 今後の改善予定
- カテゴリ別の収支集計
- 月次レポート出力
- GitHub ActionsでCIテスト自動化
- フロントエンドとの連携（Next.js予定）
