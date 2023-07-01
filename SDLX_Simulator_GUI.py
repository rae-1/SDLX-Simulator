import numpy as np
# import pandas as pd
import alu
import tkinter as tk
from tkinter import ttk
# from random import choice

def disp(inp,out,aluOutput,current_pc,next_pc):
    window1 = tk.Tk()
    window2 = tk.Tk()

    window1.geometry('600x400')
    # window1.title('Treeview')
    window1.title("RegFile")
    window2.geometry('600x400')
    window2.title('Treeview')

    # treeview 
    table1 = ttk.Treeview(window1, columns = ('first', 'mid', 'last'), show = 'headings')
    table1.heading('first', text = 'Flag')
    table1.heading('mid', text = 'Registers')
    table1.heading('last', text = 'value')
    table1.pack(fill = 'both', expand = True)

    table2 = ttk.Treeview(window2, columns = ('first', 'last'), show = 'headings')
    table2.heading('first', text = 'item')
    table2.heading('last', text = 'value')
    table2.pack(fill = 'both', expand = True)

    for i in range(32):
        if(i==inp[0] or i== inp[1]):
            table1.insert(parent='',index=i,values=("RS"+str(inp.index(i)+1),'R'+str(i),regFile[i]))    
        elif(i==out):
            table1.insert(parent='',index=i,values=("RD",'R'+str(i),regFile[i]))            
        else:
            table1.insert(parent='',index=i,values=("-",'R'+str(i),regFile[i]))   

    table2.insert(parent='',index=0,values=("aluOutput",aluOutput)) 
    table2.insert(parent='',index=1,values=("current PC",current_pc)) 
    table2.insert(parent='',index=2,values=("next PC",next_pc)) 
    
    memory_disp()
    window1.mainloop()
    window2.mainloop()
    return

def disp_RI(inp,imm,out,aluOutput,current_pc,next_pc):
    window1 = tk.Tk()
    window2 = tk.Tk()

    window1.geometry('600x400')
    # window1.title('Treeview')
    window1.title("RegFile")
    window2.geometry('600x400')
    window2.title('Treeview')

    # treeview 
    table1 = ttk.Treeview(window1, columns = ('first', 'mid', 'last'), show = 'headings')
    table1.heading('first', text = 'Flag')
    table1.heading('mid', text = 'Registers')
    table1.heading('last', text = 'value')
    table1.pack(fill = 'both', expand = True)

    table2 = ttk.Treeview(window2, columns = ('first', 'last'), show = 'headings')
    table2.heading('first', text = 'item')
    table2.heading('last', text = 'value')
    table2.pack(fill = 'both', expand = True)

    for i in range(32):
        if(i==inp):
            table1.insert(parent='',index=i,values=("RS"+str(1),'R'+str(i),regFile[i]))    
        elif(i==out):
            table1.insert(parent='',index=i,values=("RD",'R'+str(i),regFile[i]))            
        else:
            table1.insert(parent='',index=i,values=("-",'R'+str(i),regFile[i]))   

    table2.insert(parent='',index=0,values=("aluOutput",aluOutput)) 
    # table2.insert(parent='',index=1,values=("pc",pc)) 
    table2.insert(parent='',index=1,values=("immediate constant",imm))
    table2.insert(parent='',index=2,values=("current PC",current_pc)) 
    table2.insert(parent='',index=3,values=("next PC",next_pc)) 
   
    memory_disp()
    window1.mainloop()
    window2.mainloop()
    return

def disp_R_J(imm,aluOutput,branch_flag,current_pc,next_pc):
    window1 = tk.Tk()
    window2 = tk.Tk()

    window1.geometry('600x400')
    # window1.title('Treeview')
    window1.title("RegFile")
    window2.geometry('600x400')
    window2.title('Treeview')

    # treeview 
    table1 = ttk.Treeview(window1, columns = ('first', 'mid', 'last'), show = 'headings')
    table1.heading('first', text = 'Flag')
    table1.heading('mid', text = 'Registers')
    table1.heading('last', text = 'value')
    table1.pack(fill = 'both', expand = True)

    table2 = ttk.Treeview(window2, columns = ('first', 'last'), show = 'headings')
    table2.heading('first', text = 'item')
    table2.heading('last', text = 'value')
    table2.pack(fill = 'both', expand = True)
    
    for i in range(32):
        # if(i==inp):
        #     table1.insert(parent='',index=i,values=("RS",'R'+str(i),regFile[i]))    
        # elif(i==out):
        #     table1.insert(parent='',index=i,values=("RD",'R'+str(i),regFile[i]))            
        table1.insert(parent='',index=i,values=("-",'R'+str(i),regFile[i]))   

    table2.insert(parent='',index=0,values=("aluOutput",aluOutput)) 
    # table2.insert(parent='',index=1,values=("pc",pc)) 
    table2.insert(parent='',index=1,values=("signed offset",imm))
    table2.insert(parent='',index=2,values=("branch_flag",branch_flag))
    table2.insert(parent='',index=3,values=("current PC",current_pc)) 
    table2.insert(parent='',index=4,values=("next PC",next_pc)) 

    memory_disp()
    window1.mainloop()
    window2.mainloop()
    return

def disp_R_JR(inp,imm,aluOutput,branch_flag,current_pc,next_pc):
    window1 = tk.Tk()
    window2 = tk.Tk()

    window1.geometry('600x400')
    # window1.title('Treeview')
    window1.title("RegFile")
    window2.geometry('600x400')
    window2.title('Treeview')

    # treeview 
    table1 = ttk.Treeview(window1, columns = ('first', 'mid', 'last'), show = 'headings')
    table1.heading('first', text = 'Flag')
    table1.heading('mid', text = 'Registers')
    table1.heading('last', text = 'value')
    table1.pack(fill = 'both', expand = True)

    table2 = ttk.Treeview(window2, columns = ('first', 'last'), show = 'headings')
    table2.heading('first', text = 'item')
    table2.heading('last', text = 'value')
    table2.pack(fill = 'both', expand = True)
    
    for i in range(32):
        if(i==inp):
            table1.insert(parent='',index=i,values=("RS",'R'+str(i),regFile[i]))    
        # elif(i==out):
        #     table1.insert(parent='',index=i,values=("RD",'R'+str(i),regFile[i]))            
        table1.insert(parent='',index=i,values=("-",'R'+str(i),regFile[i]))   

    table2.insert(parent='',index=0,values=("aluOutput",aluOutput)) 
    # table2.insert(parent='',index=1,values=("pc",pc)) 
    table2.insert(parent='',index=1,values=("signed offset",imm))
    table2.insert(parent='',index=2,values=("branch_flag",branch_flag))
    table2.insert(parent='',index=3,values=("current PC",current_pc)) 
    table2.insert(parent='',index=4,values=("next PC",next_pc)) 

    memory_disp()
    window1.mainloop()
    window2.mainloop()
    return

def disp_R_B(inp,imm,aluOutput,branch_flag,current_pc,next_pc):
    window1 = tk.Tk()
    window2 = tk.Tk()

    window1.geometry('600x400')
    # window1.title('Treeview')
    window1.title("RegFile")
    window2.geometry('600x400')
    window2.title('Treeview')

    # treeview 
    table1 = ttk.Treeview(window1, columns = ('first', 'mid', 'last'), show = 'headings')
    table1.heading('first', text = 'Flag')
    table1.heading('mid', text = 'Registers')
    table1.heading('last', text = 'value')
    table1.pack(fill = 'both', expand = True)

    table2 = ttk.Treeview(window2, columns = ('first', 'last'), show = 'headings')
    table2.heading('first', text = 'item')
    table2.heading('last', text = 'value')
    table2.pack(fill = 'both', expand = True)

    for i in range(32):
        if(i==inp):
            table1.insert(parent='',index=i,values=("RS",'R'+str(i),regFile[i]))    
        # elif(i==out):
        #     table1.insert(parent='',index=i,values=("RD",'R'+str(i),regFile[i]))            
        else:
            table1.insert(parent='',index=i,values=("-",'R'+str(i),regFile[i]))   

    table2.insert(parent='',index=0,values=("aluOutput",aluOutput)) 
    # table2.insert(parent='',index=1,values=("pc",pc)) 
    table2.insert(parent='',index=1,values=("signed offset",imm))
    table2.insert(parent='',index=2,values=("branch_flag",branch_flag))
    # table2.insert(parent='',index=2,values=("jal_flag",jal_flag))
    table2.insert(parent='',index=3,values=("current PC",current_pc)) 
    table2.insert(parent='',index=4,values=("next PC",next_pc)) 
   
    memory_disp()
    window1.mainloop()
    window2.mainloop()
    return

def disp_R_JALR(inp,imm,aluOutput,branch_flag,jal_flag,current_pc,next_pc):
    window1 = tk.Tk()
    window2 = tk.Tk()

    window1.geometry('600x400')
    # window1.title('Treeview')
    window1.title("RegFile")
    window2.geometry('600x400')
    window2.title('Treeview')

    # treeview 
    table1 = ttk.Treeview(window1, columns = ('first', 'mid', 'last'), show = 'headings')
    table1.heading('first', text = 'Flag')
    table1.heading('mid', text = 'Registers')
    table1.heading('last', text = 'value')
    table1.pack(fill = 'both', expand = True)

    table2 = ttk.Treeview(window2, columns = ('first', 'last'), show = 'headings')
    table2.heading('first', text = 'item')
    table2.heading('last', text = 'value')
    table2.pack(fill = 'both', expand = True)

    for i in range(32):
        if(i==inp):
            table1.insert(parent='',index=i,values=("RS",'R'+str(i),regFile[i]))    
        # # elif(i==out):
        # #     table1.insert(parent='',index=i,values=("RD",'R'+str(i),regFile[i]))            
        else:
            table1.insert(parent='',index=i,values=("-",'R'+str(i),regFile[i]))   

    table2.insert(parent='',index=0,values=("aluOutput",aluOutput)) 
    # table2.insert(parent='',index=1,values=("pc",pc)) 
    table2.insert(parent='',index=1,values=("signed offset",imm))
    table2.insert(parent='',index=2,values=("branch_flag",branch_flag))
    table2.insert(parent='',index=3,values=("jal_flag",jal_flag))
    table2.insert(parent='',index=4,values=("current PC",current_pc)) 
    table2.insert(parent='',index=5,values=("next PC",next_pc)) 

    memory_disp()
    window1.mainloop()
    window2.mainloop()
    return

def disp_R_JAL(imm,aluOutput,branch_flag,jal_flag,current_pc,next_pc):
    window1 = tk.Tk()
    window2 = tk.Tk()

    window1.geometry('600x400')
    # window1.title('Treeview')
    window1.title("RegFile")
    window2.geometry('600x400')
    window2.title('Treeview')

    # treeview 
    table1 = ttk.Treeview(window1, columns = ('first', 'mid', 'last'), show = 'headings')
    table1.heading('first', text = 'Flag')
    table1.heading('mid', text = 'Registers')
    table1.heading('last', text = 'value')
    table1.pack(fill = 'both', expand = True)

    table2 = ttk.Treeview(window2, columns = ('first', 'last'), show = 'headings')
    table2.heading('first', text = 'item')
    table2.heading('last', text = 'value')
    table2.pack(fill = 'both', expand = True)

    for i in range(32):
        # if(i==inp):
        #     table1.insert(parent='',index=i,values=("RS",'R'+str(i),regFile[i]))    
        # # elif(i==out):
        # #     table1.insert(parent='',index=i,values=("RD",'R'+str(i),regFile[i]))            
        table1.insert(parent='',index=i,values=("-",'R'+str(i),regFile[i]))   

    table2.insert(parent='',index=0,values=("aluOutput",aluOutput)) 
    # table2.insert(parent='',index=1,values=("pc",pc)) 
    table2.insert(parent='',index=1,values=("signed offset",imm))
    table2.insert(parent='',index=2,values=("branch_flag",branch_flag))
    table2.insert(parent='',index=3,values=("jal_flag",jal_flag))
    table2.insert(parent='',index=4,values=("current PC",current_pc)) 
    table2.insert(parent='',index=5,values=("next PC",next_pc)) 

    memory_disp()
    window1.mainloop()
    window2.mainloop()
    return

def memory_disp ():
    global memory
    temp_memory={}
    for i in range(100):
        temp_memory[i] = memory[i][:8] + "  " + memory[i][8:16] + "  " + memory[i][16:24] + "  " + memory[i][24:]
    
    window1 = tk.Tk()
    window1.geometry('600x400')
    # window1.title('Treeview')
    window1.title("Memory Data")

    # j=256
    # for i in range(64,100):
    #     temp_memory[i] = ((bin(j)[2:]).zfill(16)) +" "+ ((bin(j+1)[2:]).zfill(16))
    #     j += 2

     # treeview 
    table1 = ttk.Treeview(window1, columns = ('first', 'last'),show = "headings")
    table1.heading('first', text = 'Address')
    table1.heading('last', text = "         00          01          10          11        ")
    table1.pack(fill = 'both', expand = True)

    i=0
    while i<100:
        table1.insert(parent='',index=i,values=(i,temp_memory[i]))
        i=i+1;   

    window1.mainloop()
    return


#<!--- ---------------------------------------------------------------------------------------------------->


def instructionType(instruction, regFile, pc):

    global branch_flag
    global JumpandLink_flag
    global count

    global curr_pc, next_pc

    opCode = instruction[0 : 6]

    if(opCode == "000000"):                                                     #R type triadic
        RS1         = int(instruction[6  : 11], 2)
        RS2         = int(instruction[11 : 16], 2)
        RD          = int(instruction[16 : 21], 2)
        operation   = int(instruction[27 : 32], 2)

        # print(instruction)
        # print("Function_Code:", operation)

        d1out       = regFile[RS1]
        d2out       = regFile[RS2]
        pc          = pc + 1

        aluOutput   = alu.compute(d1out, d2out, operation)
        regFile[RD] = aluOutput
        inp=[RS1,RS2]
        out=RD
        
        print("RS1:",RS1, ", RS2:", RS2, ", RD:", RD)
        print("Function_Code:", operation)
        print("D1 0ut:",d1out, ", D2 Out:",d2out, ", Din:", aluOutput, "\n")

        regFile[0] = 0
        disp(inp,out,aluOutput,curr_pc,next_pc)
        # memory_disp()
        return aluOutput, pc

    elif(opCode[0] == "1"):                                                     # R-I type triadic
        RS1         = int(instruction[6  : 11], 2)
        RD          = int(instruction[11 : 16], 2)
        immediate   = instruction[16 : 32]
        operation   = int(instruction[0  : 6], 2)

        # extendedImmediate = int(immediate[0] * 16 + immediate, 2)
        extendedImmediate = int(immediate[1:],2) - int(immediate[0],2)*(2**15)

        d1out       = regFile[RS1]
        pc          = pc + 1
        

        if operation<20:                                                        # ALU operations
            aluOutput   = alu.compute(d1out, extendedImmediate, operation)
            regFile[RD] = aluOutput

            print("ALU output", aluOutput)

        else:                                                                   # Data Transfer Instructions
            aluOutput  = alu.compute(d1out, extendedImmediate, alu.ADD)
            memory_Address = aluOutput//4
            # memory_Address = aluOutput[:30]

            opCode = int(opCode, 2)
            last2 = int( aluOutput % 4 )
            # last2 = int( aluOutput[30:32], 2 )

            ## Big-endian is used to store data

            if (opCode == alu.LH or opCode == alu.LHU or opCode == alu.SH) and (last2 == 1 or last2 == 3):
                raise Exception ("Unaligned Access")
            
            elif (opCode == alu.LW or opCode == alu.SW) and (last2 == 1 or last2 == 2 or last2 == 3):
                raise Exception ("Unaligned Access")

            ## Load operations
            if opCode == alu.LB:
                data = memory[memory_Address][last2*8 : (last2+1)*8]
                # signExtended_data = int(data[0] * 24 + data, 2)
                signExtended_data = int(data[1:],2) - int(data[0],2)*(2**7)

                regFile[RD] = signExtended_data

            elif opCode == alu.LBU:
                data = memory[memory_Address][last2*8 : (last2+1)*8]
                padded_data = int("0" * 24 + data, 2)

                regFile[RD] = padded_data

            elif opCode == alu.LH:
                data = memory[memory_Address][last2*8 : (last2+2)*8]
                # signExtended_data = int(data[0] * 16 + data, 2)
                signExtended_data = int(data[1:],2) - int(data[0],2)*(2**15)

                regFile[RD] = signExtended_data

            elif opCode == alu.LHU:
                data = memory[memory_Address][last2*8 : (last2+2)*8]
                padded_data = int("0" * 16 + data, 2)

                regFile[RD] = padded_data

            elif opCode == alu.LW:
                data = memory[memory_Address][last2*8 : (last2+4)*8]

                regFile[RD] = data

            ## Store Operations
            
            # else:
            #     data = regFile[RD]
            #     memory[memory_Address] = data

            elif opCode == alu.SB:
                # data = str(regFile[RD])[24:32].zfill(8)
                if regFile[RD]>=0:
                    data = bin(regFile[RD])[2:].zfill(8)
                else:
                    data = bin(2**8+regFile[RD])[2:]

                memory_value = memory[memory_Address]
                arr = list(memory_value)
                if last2==0:
                    arr[:8] = data
                elif last2==1:
                    arr[8:16] = data
                elif last2==2:
                    arr[16:24] = data
                else:
                    arr[24:32] = data
                memory_value = "".join(arr)

                memory[memory_Address] = memory_value
            
            elif opCode == alu.SH:
                # data = str(regFile[RD])[16:32].zfill(16)
                if regFile[RD]>=0:
                    data = bin(regFile[RD])[2:].zfill(16)
                else:
                    data = bin(2**16+regFile[RD])[2:]

                memory_value = memory[memory_Address]
                arr = list(memory_value)
                if last2==0:
                    arr[:16] = data
                else:
                    arr[16:32] = data
                memory_value = "".join(arr)

                memory[memory_Address] = memory_value

            elif opCode == alu.SW:
                print("old value at memory location", memory[memory_Address])
                data = regFile[RD]
                memory[memory_Address] = (bin(data)[2:]).zfill(32)
                print("decimal value stored", data)

            print("register value:", regFile[RD])
        
        regFile[0] = 0
        disp_RI(RS1,immediate,RD,aluOutput,curr_pc,next_pc)
        # memory_disp()
        return aluOutput, pc

    else:
        ## R diadic
        opCode = int(opCode, 2)
        offset = instruction[16:32]
        # extendedOffset = int(offset[0] * 16 + offset, 2)
        extendedOffset = int(offset[1:],2) - int(offset[0],2)*(2**15)
        
        if opCode==alu.BEQZ:
            if regFile[RS1]==0:
                aluOutput = alu.compute(4*(pc+1) , extendedOffset, alu.ADD4)
                pc = aluOutput//4
                branch_flag = 1

            else:
                pc = pc + 1
                aluOutput = None

            disp_R_B(RS1,offset,aluOutput,branch_flag)
            # memory_disp()

        elif opCode==alu.BNEZ:
            if regFile[RS1]!=0:
                aluOutput = alu.compute(4*(pc+1) , extendedOffset, alu.ADD4)
                pc = aluOutput//4
                branch_flag = 1

            else:
                pc = pc + 1
                aluOutput = None

            disp_R_B(RS1,offset,aluOutput,branch_flag,curr_pc,next_pc)
            # memory_disp()

        elif opCode==alu.JR:
            RS1       = int(instruction[6:11], 2)
            if regFile[RS1]>=0:
                RS1_value = int(((bin(regFile[RS1])[2:]).zfill(32))[:30]+"00",2)
            else:
                RS1_value = int(4*(regFile[RS1]//4))

            aluOutput = alu.compute(RS1_value , extendedOffset, alu.ADD4)
            pc = aluOutput//4
            branch_flag = 1
            disp_R_JR(RS1,offset,aluOutput,branch_flag,curr_pc,next_pc)
            # memory_disp()
            
        elif opCode==alu.JALR:
            RS1       = int(instruction[6:11], 2)
            if regFile[RS1]>=0:
                RS1_value = int(((bin(regFile[RS1])[2:]).zfill(32))[:30]+"00",2)
            else:
                RS1_value = int(4*(regFile[RS1]//4))
            regFile[31] = pc + 2

            aluOutput = alu.compute(RS1_value , extendedOffset, alu.ADD4)
            pc = aluOutput//4
            branch_flag = 1
            JumpandLink_flag = 1
            disp_R_JALR(RS1,offset,aluOutput,branch_flag,JumpandLink_flag,curr_pc,next_pc)
            # memory_disp()

        else: pass

        ## J type
        signed_offset = instruction[6:32]
        # extended_signed_offset = int(signed_offset[0] * 6 + signed_offset, 2)
        extended_signed_offset = int(signed_offset[1:], 2) - int(signed_offset[0],2)*(2**25)

        if opCode==alu.J:
            aluOutput = alu.compute(4*(pc+1) , extended_signed_offset, alu.ADD4)
            pc = aluOutput//4
            branch_flag = 1
            disp_R_J(signed_offset,aluOutput,branch_flag,curr_pc,next_pc)
            # memory_disp()

        elif opCode==alu.JAL:
            regFile[31] = pc + 2
            aluOutput = alu.compute(4*(pc+1) , extended_signed_offset, alu.ADD4)
            pc = aluOutput//4
            branch_flag = 1
            JumpandLink_flag = 1
            print("updated R31:", regFile[31])
            disp_R_JAL(signed_offset,regFile[31],aluOutput,branch_flag,JumpandLink_flag,curr_pc,next_pc)
            # memory_disp()

        regFile[0] = 0
        return aluOutput, pc

    regFile[0] = 0
    return None, None


with open('C:\\Users\\Yashraj Deshmukh\\Desktop\\COA project\\instructions.txt', 'rb') as file:
    # print()

    next_pc        =  100
    aluOutput      =  None
    memory_Address =  None

    regFile = np.zeros(32, dtype=int)
    for i in range(0, 32):
        regFile[i] = i
        # if i==20:
        #     regFile[i] = -5

    memory = {}
    for i in range(64):
        memory[i] = ((bin(4*i)[2:]).zfill(8)) + ((bin(4*i+1)[2:]).zfill(8)) + (bin(4*i+2)[2:]).zfill(8) + (bin(4*i+3)[2:]).zfill(8)

    j=256
    for i in range(64,100):
        memory[i] = ((bin(j)[2:]).zfill(16)) + ((bin(j+1)[2:]).zfill(16))
        j += 2

    for instruction in file:
        PC, instruction_code = map( lambda n:n, instruction.split() )
        memory[int(PC)] = str(instruction_code).replace("_", "")

    # print(memory)
    
    branch_flag      = 0
    JumpandLink_flag = 0
    count            = 0
    
    while int(input()):
        curr_pc = next_pc

        if branch_flag==1:
            next_pc = output_pc
            count = 1
            branch_flag = 0

        elif count==1 and JumpandLink_flag==1:
            next_pc = regFile[31]
            JumpandLink_flag = 0
            count = 0

        else:
            next_pc = curr_pc + 1
            count = 0

        try:
            instruction = memory[curr_pc][2:34]
        except:
            raise Exception("No further instruction found")

        print("current PC:", curr_pc, ", next_pc:", next_pc)

        print(curr_pc, ":", instruction)

        result, output_pc = instructionType(instruction, regFile, curr_pc)

        # print("aluOutput : ", result, ", Next PC : ", output_pc)

        # print("Content of regfile")
        # for i in range (0, 32):
        #     print(regFile[i], end=" ")
        # print("\n")


# <!--- ----------------------------------------------------------------->

