# Smart Scroll — Android APK 配布ページ

こちらは Smart Scroll の配布用公開ページです。開発コードは別の非公開リポジトリで管理しています。

## 共通インストール用 QR コード

![Smart Scroll 共通インストール QR コード](./SmartScroll-common-QR.png)

**[QR コード画像を直接開く（PNG）](https://github.com/sui-0825/smart-scroll-apk/blob/main/SmartScroll-common-QR.png)**

この QR コードはバージョンごとの APK ではなく、[Releases（公開版一覧）](https://github.com/sui-0825/smart-scroll-apk/releases) に移動します。新しいバージョンが追加されても同じ QR コードを使えます。

## 公開状況（2026-10-17）

- 現在の配布物：**v0.4.6（Pre-release / テスト版）**
- Android 端末 1 台で、v0.4.5 → v0.4.6 の更新通知・上書き・設定維持・ユーザー補助の設定維持を確認済み。
- 動画判定・自動スワイプの正確さ、異なるメーカーの端末での動作は十分な検証ができていません。少数のテスト端末から試してください。

## インストール手順

1. QR コードから Releases にアクセス
2. 最新の対象リリースを開き、**Assets** にある `SmartScroll-vX.Y.Z.apk` を選択（ZIP や Source code ではありません）
3. Android の案内を読んでインストールを承認
4. アプリで通知権限および必要なユーザー補助権限を確認
5. 対象アプリとルールを設定して、まず 1 台で開始・停止をテスト

更新は各端末で選択式です。インストールを勝手に実行しません。更新チェックは約 6 時間ごとで、Android の省電力設定やネット接続により遅れる場合があります。

**注意:** Android のユーザー補助は強力な権限です。信頼できる APK かを確認し、端末の安全設定や対象アプリの規約に従ってください。開発コード・D&D アプリ・猫監視アプリとは連携していません。
