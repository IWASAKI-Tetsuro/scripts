#!/usr/bin/perl

# this script will output lines between "x" and "y"
# inport hspice .lis file from stdin or argument
# output doesn't have header, please write the header by yourself

use strict;
use warnings;
use Getopt::Long;

Getopt::Long::Configure('bundling');

my $sep = ","; # csv mode
my $block = 0; # if block is 1, the empty row is inserted between xy blocks.

GetOptions(
  'sep|s=s' => \$sep,
  'block|b' => \$block,
) or die "Incorrect option.";
$sep =~ s/\\t/\t/g;

my $flag = 0; # if flag is 1, the line will be outputted.
while(<>){ # input from standard input or argument

  if(/^\s*y\s*$/){
    if(${block} == 1){
    print "\n";
      }
    $flag = 0;
    }

  if($flag == 1 && /\S/){
    if(/^\s*-*\d/){ # extract data lines
      chomp;
      s/^\s+|\s+$//g; #deleat head space and trail space
        s/\s+/$sep/g; #swap all space charactor to $sep
      
      print "$_\n"; #print modyfied lines
		}
	}
 
  if(/\s*^x\s*$/){
    $flag = 1;
  }

}

