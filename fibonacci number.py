def fibonacci(n):
    #base case
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    #recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    # İlk n Fibonacci sayısını hesaplamak ve yazdırmak için
def fibonacci_series(n):
    #series.append(fibonacci(i)) ifadesi, fibonacci(i) fonksiyonunun i'nci Fibonacci sayısını döndürmesini sağlar ve bu değeri series listesinin sonuna ekler.
    series = []
    for i in range(n):
        series.append(fibonacci(i))
    return series 
 
while True:
    try:
        user_input = input("Enter a number (type 'a' to quit): ")
        if user_input.lower() == 'a':
            break
        n = int(user_input)
        result = fibonacci_series(n)
        print(f"The first {n} Fibonacci numbers are: {result}")
        #f" ve " işaretleri arasındaki metin, f-string olarak adlandırılan bir biçimlendirilmiş string ifadesidir.^
        #Bu, string içinde Python ifadelerini {} içinde değerlendirmenize olanak tanır.
        #{n} ifadesi, n değişkeninin değerini string içinde yerleştirir.
        #{result} ifadesi, result listesinin tamamını string içinde yerleştirir.
        if n > 1:
            print(f"Fibonacci({n}) = {result[-1]}") #Eğer n 1'den büyükse, serinin son elemanını yazdırırız. 
            #result[-1] ifadesi, result listesinin son elemanını ifade eder. Örneğin, n 10 ise result[-1] 34 olur.
        else:
            print(f"Fibonacci({n}) = {result[0]}") #print(f"Fibonacci({n}) = {result[0]}") satırı, n'inci Fibonacci sayısını yazdırır.

    except ValueError:
        print("Invalid input, please enter a number.")

              
    
        
             

      







