# 作り方
1. エンドポイントを作る
1. リクエストパラメータをschemaで定義する
1. レスポンスパラメータをschemaで定義する←ここまででいったんdocはできるはず
1. crudsを定義する

# 設計

## DB
### table
#### m_users
- id
- name
- image
- created_at
- updated_at
#### m_projects
- id
- name
- description
- sale_cost
- planned_release_date
- fact_release_date
- created_at
- updated_at
#### t_milestone
- id
- project_id
- assign_user_id
- progre_flag
- assign_start_date
- assign_end_date

# dockerのwebの方でpackageがインストールできない場合
- vi /etc/resolv.conf
  - 8.8.8.8追加

# 参考
- https://zenn.dev/sh0nk/books/537bb028709ab9/viewer/0a38c1
- https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5
- https://zenn.dev/tet0h/articles/docker-vuejs

# migrate
- apiコンテナ内で
  - python -m migrate_db