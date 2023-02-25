CREATE TABLE users(
    id INT IDENTITY,
    username NVARCHAR(20),
    password NVARCHAR(50),
    fullname NVARCHAR(40)
)

INSERT INTO users 
	VALUES ('Cebrian10', '1234', 'Ameth Cebrian')
	
Select *
	From users
          
Drop Table users