INSERT INTO users (full_name, email, password)
VALUES
('Aselya', 'aselya@gmail.com', '12345'),
('Aiasyl', 'aiasyl@gmail.com', '54321');

INSERT INTO books (title, author, year, available)
VALUES
('Harry Potter', 'J.K Rowling', 2001, TRUE),
('Atomic Habits', 'James Clear', 2018, TRUE);

INSERT INTO orders (user_id, book_id, order_date)
VALUES
(1, 1, '2026-05-28');