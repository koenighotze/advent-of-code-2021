use strict;
use warnings;

my @input = <STDIN>;
@input = map { chomp(); $_ } @input; 

sub most_common_bit_at {
    my $target_column = shift;
    my @data = @_;

    print "Trying to find most common bit in column $target_column\n";

    my @bits;
    foreach my $line (@data) {
        chomp($line);

        my $value = substr($line, $target_column, 1);
        $bits[0] or $bits[0] = 0;
        $bits[1] or $bits[1] = 0;
        $bits[$value]++;
    }

    return $bits[0] > $bits[1] ? 0 : 1;
}

sub oxygen {
    my $target_column = shift;
    my @data = @_;

    my $mcb = most_common_bit_at($target_column, @data);
    my @candidates = grep { substr($_, $target_column, 1) eq $mcb } @data;

    if (scalar @candidates > 1) {
        return oxygen($target_column + 1, @candidates);
    }
    return $candidates[0];
}

sub scrubber {
    my $target_column = shift;
    my @data = @_;

    my $mcb = most_common_bit_at($target_column, @data);
    print "MCB: $mcb\n";
    my @candidates = grep { substr($_, $target_column, 1) ne $mcb } @data;

    print "Reduced to: \n";
    print join(" \n", @candidates);
    print "\n";

    if (scalar @candidates > 1) {
        return scrubber($target_column + 1, @candidates);
    }
    return $candidates[0];
}

my $ox = "0b".oxygen(0, @input);
print "Oxygen $ox\n\n\n\n\n";
my $scrub = "0b".scrubber(0, @input);
print "Scrubber $scrub\n";

my $result = oct($ox) * oct($scrub);
print "Result: $result\n";