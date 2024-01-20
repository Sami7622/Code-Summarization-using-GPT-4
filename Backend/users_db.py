from database import create_connection
from user import User

con = create_connection()
database = con.cursor()

class users_db:
    def modify_user(self, users_list):
        user_details = User(users_list[0], users_list[1], users_list[2], users_list[3], users_list[4], users_list[5])
        return user_details

    def get(self, email):
        try:
            print(email)
            query = "SELECT * FROM users WHERE email = %s"
            database.execute(query, (email,))
            result = database.fetchone()
            print(result)
            if result:
                return self.modify_user(result)  # User details as a dictionary
            else:
                return None  # User not found
        except Exception as e:
            # Handle database errors here, e.g., logging or raising an exception
            raise e
    def updatePassword(self, email,password):
        try:
            print(email)
            database.execute("UPDATE users SET passwordHash = %s WHERE email = %s", (password, email))
            con.commit()
                
            return {"message": "password Update sucessfully"}  # User details as a dictionary
                
        except Exception as e:
            # Handle database errors here, e.g., logging or raising an exception
            raise e
    
    def update_verified_in_db(self,email: str):
        update_query = "UPDATE users SET verified = 1 WHERE email = %s"
        try:
                    database.execute(update_query, (email,))
                    con.commit()
        except pymysql.Error as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

