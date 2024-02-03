#%%
import warnings
warnings.filterwarnings('ignore',message="Reloaded modules: db_lib")
#%%
import mysql.connector
 
global cnx

try:
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="*071298*aA",
        database="pandeyji_eatery"
    )
    print('Veritabanına başarı ile bağlanıldı')
except mysql.connector.Error as err:
    print(f'Hata: {err}')
    
    
def get_order_status(order_id: int):
    
    cursor=cnx.cursor()
    
    query =("SELECT status FROM order_tracking WHERE  order_id = %s")
    
    cursor.execute(query,(order_id,))
    
    result= cursor.fetchone()
    
    cursor.close()
    cnx.close()
    
    if result is not None:
        return result[0]
    else:
        return None
    
    
    