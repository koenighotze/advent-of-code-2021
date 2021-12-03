use strict;
use warnings;

my @gammas = ();
while (my $line = <STDIN>) {
    chomp($line);
    my $col = 0;
    foreach (split(//, $line)) {        
        $gammas[$col][0] or $gammas[$col][0] = 0;
        $gammas[$col][1] or $gammas[$col][1] = 0;
        $gammas[$col][$_]++;
        $col ++;
    }
}

my $gamma = "0b";
my $epsilon = "0b";
foreach my $c (@gammas) {
    $gamma .= ($$c[1] > $$c[0]) ? 1 : 0;
    $epsilon .= ($$c[1] > $$c[0]) ? 0 : 1;    
}

print "Gamma bitstring $gamma\n";
print "Epsilon bitstring $epsilon\n";
my $result = oct($gamma) * oct($epsilon);
print "Result: $result\n";

