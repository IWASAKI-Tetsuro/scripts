#!/usr/bin/perl

use strict;
use warnings;
my $max_value = 0;
my $min_value = 1000000000;
my $max_a = 0;
my $max_b = 0;
my $min_a = 0;
my $min_b = 0;

while(<>){
  chomp;
  my @line = split(/\s+/, $_);

  if ($max_value <= $line[2]){
    $max_value = $line[2];
    $max_a = $line[0];
    $max_b = $line[1];
  }

  if ($min_value >= $line[2]){
    $min_value = $line[2];
    $min_a = $line[0];
    $min_b = $line[1];
  }
}

print "max = $max_value at ($max_a, $max_b)\n";
print "min = $min_value at ($min_a, $min_b)\n";
