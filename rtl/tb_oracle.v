`timescale 1ns/1ps
module tb_oracle;
  reg [31:0] a,b,expected;
  reg [2:0] op;
  wire [31:0] y;
  alu dut(.a(a),.b(b),.op(op),.y(y));
  integer fd,rc,n=0;
  initial begin
    fd=$fopen("build/vectors.txt","r");
    if(!fd) $fatal(1,"vectors missing");
    while(!$feof(fd)) begin
      rc=$fscanf(fd,"%h %h %h %h\n",a,b,op,expected);
      if(rc!=4) $fatal(1,"malformed vector");
      #1;
      if(y !== expected) $fatal(1,"ALU mismatch opcode=%0d a=%h b=%h got=%h expected=%h",op,a,b,y,expected);
      n=n+1;
    end
    $display("PASS: %0d independent ALU oracle vectors",n);
    $finish;
  end
  initial begin #20000; $fatal(1,"oracle watchdog"); end
endmodule
