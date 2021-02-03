CREATE TABLE IF NOT EXISTS tasks (
    task_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    start_date DATE,
    due_date DATE,
    status TINYINT NOT NULL,
    priority TINYINT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)  ENGINE=INNODB;


CREATE INDEX due_date_btree USING BTREE ON tasks (due_date);
CREATE INDEX start_date_hash USING HASH ON tasks (start_date);

OPTIMIZE TABLE tasks;
