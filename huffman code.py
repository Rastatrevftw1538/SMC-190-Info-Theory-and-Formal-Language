import re

##def main():
##    sys_input = input("Insert messege with symbols A-F: ")
##    regex = re.compile(r".")
##    frequ = {}
##    frequ_tot = 0
##    ccc = frequ.get(float(len(frequ))-float(len(frequ))-1)
##    code = ""
##    sys_val= {}
##    #sys_val= {"A":"11","B":"01","C":"00","D":"101","E":"1001","F":"1000"}
##    val = sys_val.values()
##
##    for aaa in regex.finditer(sys_input):
##        try:
##            frequ[aaa.group(0)] += 1
##        except KeyError:
##            frequ[aaa.group(0)] = 1
##    print(frequ)
##    
##    for fff in frequ:
##        frequ_tot = frequ.get(fff) + frequ_tot
##    print(frequ_tot)
##    for eee in frequ:
##        ccc = frequ_tot - frequ.get(eee)
##        while ccc >= 0:
##            print(ccc)
##            print(frequ_tot/2)
##            if ccc >= frequ_tot/2:
##                code += "1"
##                ccc -= ccc + frequ_tot
##                print(code)
##                continue
##            else:
##                code += "0"
##                ccc -= ccc + frequ_tot
##                print(code)
##                continue
##        sys_val.update({eee:code})
##        code = ""
##        print(sys_val)
##    #for i in sys_input:
##        #for x in sys_val:
##            #if i == x:
##                #v = sys_input.replace(i,sys_val[x])
##        #sys_input = v
##    #print(v)
##
##
##main()

class HuffmanCoding:
        def __init__(self, path):
                self.path = path
                self.heap = []
                self.codes = {}
                self.reverse_mapping = {}
                
        # functions for compression:

        def make_frequency_dict(self, text):
                frequency = {}
                for character in text:
                        if not character in frequency:
                                frequency[character] = 0
                        frequency[character] += 1
                return frequency

        def make_heap(self, frequency):
                for key in frequency:
                        node = HeapNode(key, frequency[key])
                        heapq.heappush(self.heap, node)

        def merge_nodes(self):
                while(len(self.heap)>1):
                        node1 = heapq.heappop(self.heap)
                        node2 = heapq.heappop(self.heap)

                        merged = HeapNode(None, node1.freq + node2.freq)
                        merged.left = node1
                        merged.right = node2

                        heapq.heappush(self.heap, merged)


        def make_codes_helper(self, root, current_code):
                if(root == None):
                        return

                if(root.char != None):
                        self.codes[root.char] = current_code
                        self.reverse_mapping[current_code] = root.char
                        return

                self.make_codes_helper(root.left, current_code + "0")
                self.make_codes_helper(root.right, current_code + "1")


        def make_codes(self):
                root = heapq.heappop(self.heap)
                current_code = ""
                self.make_codes_helper(root, current_code)


        def get_encoded_text(self, text):
                encoded_text = ""
                for character in text:
                        encoded_text += self.codes[character]
                return encoded_text


        def pad_encoded_text(self, encoded_text):
                extra_padding = 8 - len(encoded_text) % 8
                for i in range(extra_padding):
                        encoded_text += "0"

                padded_info = "{0:08b}".format(extra_padding)
                encoded_text = padded_info + encoded_text
                return encoded_text


        def get_byte_array(self, padded_encoded_text):
                if(len(padded_encoded_text) % 8 != 0):
                        print("Encoded text not padded properly")
                        exit(0)

                b = bytearray()
                for i in range(0, len(padded_encoded_text), 8):
                        byte = padded_encoded_text[i:i+8]
                        b.append(int(byte, 2))
                return b


        def compress(self):
                filename, file_extension = os.path.splitext(self.path)
                output_path = filename + ".bin"

                with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
                        text = file.read()
                        text = text.rstrip()

                        frequency = self.make_frequency_dict(text)
                        self.make_heap(frequency)
                        self.merge_nodes()
                        self.make_codes()

                        encoded_text = self.get_encoded_text(text)
                        padded_encoded_text = self.pad_encoded_text(encoded_text)

                        b = self.get_byte_array(padded_encoded_text)
                        output.write(bytes(b))

                print("Compressed")
                return output_path


        """ functions for decompression: """

        def remove_padding(self, padded_encoded_text):
                padded_info = padded_encoded_text[:8]
                extra_padding = int(padded_info, 2)

                padded_encoded_text = padded_encoded_text[8:] 
                encoded_text = padded_encoded_text[:-1*extra_padding]

                return encoded_text

        def decode_text(self, encoded_text):
                current_code = ""
                decoded_text = ""

                for bit in encoded_text:
                        current_code += bit
                        if(current_code in self.reverse_mapping):
                                character = self.reverse_mapping[current_code]
                                decoded_text += character
                                current_code = ""

                return decoded_text


        def decompress(self, input_path):
                filename, file_extension = os.path.splitext(self.path)
                output_path = filename + "_decompressed" + ".txt"

                with open(input_path, 'rb') as file, open(output_path, 'w') as output:
                        bit_string = ""

                        byte = file.read(1)
                        while(byte != ""):
                                byte = ord(byte)
                                bits = bin(byte)[2:].rjust(8, '0')
                                bit_string += bits
                                byte = file.read(1)

                        encoded_text = self.remove_padding(bit_string)

                        decompressed_text = self.decode_text(encoded_text)
                        
                        output.write(decompressed_text)

                print("Decompressed")
                return output_path
HuffmanCoding()
