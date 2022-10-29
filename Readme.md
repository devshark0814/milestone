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


# 参考
- https://zenn.dev/sh0nk/books/537bb028709ab9/viewer/0a38c1
- https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5

``` sql
-- milestone.m_projects definition

CREATE TABLE `m_projects` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `sale_cost` int(10) unsigned DEFAULT 0,
  `planned_release_date` datetime DEFAULT NULL,
  `fact_release_date` datetime DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- milestone.m_users definition

CREATE TABLE `m_users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- milestone.t_milestones definition

CREATE TABLE `t_milestones` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` bigint(20) unsigned NOT NULL,
  `assign_user_id` bigint(20) unsigned NOT NULL,
  `progre_flag` tinyint(1) DEFAULT 0,
  `assign_start_date` datetime NOT NULL,
  `assign_end_date` datetime NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```