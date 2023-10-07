# Bir bağlı liste (linked list), verileri birbirine bağlı düğümler veya düğüm çiftleri (node) aracılığıyla saklayan bir veri yapısıdır. Her düğüm, bir veri öğesini (veri alanı) ve bir sonraki düğümün referansını (pointer veya link) içerir. Temel bağlı liste özellikleri ve ne zaman kullanmanızın optimum olduğu durumlar şunlardır:

# Temel Bağlı Liste Özellikleri:

# Bağlantılı Yapı: Bağlı listeler, verilerin ardışık bellek bölgelerinde değil, birbirine bağlı düğümler aracılığıyla saklandığı veri yapılardır. Bu, veri eklemesi ve çıkarması için daha esnek bir yapı sunar.

# Dinamik Büyüklük: Bağlı listeler, başlangıçta belirli bir boyuta sahip olmak zorunda değildir ve dinamik olarak büyüyebilirler. Bu, dinamik veri gereksinimlerini karşılamak için uygundur.

# Karmaşıklık: Bağlı listelerin bazı işlemleri (örneğin, başa veya sona ekleme) sabit zamanlı (O(1)) olabilir. Ancak, belirli bir düğümü aramak veya belirli bir pozisyondaki düğümü silmek gibi işlemler için O(n) zaman karmaşıklığına sahip olabilirler.

# Ne Zaman Bağlı Liste Kullanmalısınız:

# Dinamik Veri Boyutu: Veri boyutu önceden bilinmiyorsa veya veri boyutu zamanla değişiyorsa, bağlı listeler uygun bir seçenek olabilir. Dizi gibi sabit boyutlu veri yapıları, veri büyüdükçe sınırlamalara yol açabilir.

# Sık Veri Ekleme veya Çıkarma İşlemleri: Veri ekleme veya çıkarma işlemleri sık sık gerçekleştiriliyorsa, bağlı listeler daha etkili olabilir. Özellikle başa veya sona eleman ekleme veya çıkarma işlemleri için sabit zamanlı (O(1)) karmaşıklığa sahiptirler.

# Bellek Verimliliği: Bağlı listeler, bellek kullanımını optimize etmek için kullanılabilir. Özellikle düğümler yalnızca veri ve bir sonraki düğümün referansını içerdiğinden, boş bir düğüm için ekstra bellek kullanımı yoktur.

# Sıralama Gereksinimleri Yoksa: Eğer verileri sıralamaya gerek yoksa ve verilerin sırası önemli değilse, bağlı listelerin diziye göre avantajları vardır. Dizi, verilerin ardışık bir sırayla saklandığı ve sıralı bir şekilde erişilebildiği bir veri yapısıdır.

# Bağlı listeler, genellikle sabit boyutlu dizilerin kısıtlamalarından kaçınmak ve veriye dinamik olarak erişim sağlamak için kullanılır. Ancak, belirli işlemler için zaman karmaşıklığının yüksek olabileceğini unutmayın, bu nedenle kullanmadan önce gereksinimlerinizi dikkatlice değerlendirmeniz önemlidir.



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

        return True

    def pop(self, value):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_First(self):

        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    
    
    def insert(self,index,value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next 
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_First()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



my_linked_list = LinkedList(1)


my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
# my_linked_list.prepend(3)

# print(my_linked_list.remove(2), '\n')

my_linked_list.reverse()


# print('Head next:', my_linked_list.head.next.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
my_linked_list.print_list()


# print(my_linked_list.get(2))




