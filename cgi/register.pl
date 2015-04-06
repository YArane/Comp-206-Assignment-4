#!/usr/bin/perl

use strict;
use CGI ':standard';

my $file = '../databases/members.csv';

sub checkUsernameExistence {
  open(INFO, "<$file");
  my @lines = <INFO>;
  close(INFO);

  foreach my $line (@lines) {
    #print "$line";

    my @words = split(/\s+/, $line);

    if (@words[0] eq @_[0]) {
      return 1;
    } 
    
  }
  return 0;
}

sub writeNewUserToDB {
  open(my $fh, '+>>', $file);
  print $fh "\n@_[0] @_[1]";
  close $fh;
}

sub main {
  my $x = checkUsernameExistence("klk");

  if ($x == 0) {
    writeNewUserToDB("peopfhjsdhjfsle", "hey");
  }

  $query = $ENV{QUERY_STRING};

  print "Content-Type:text/html;charset=iso-8859-1";
  print "<TITLE>$query</TITLE>";
}

main();

