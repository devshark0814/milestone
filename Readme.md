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


# 参考
- https://zenn.dev/sh0nk/books/537bb028709ab9/viewer/0a38c1
- https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5