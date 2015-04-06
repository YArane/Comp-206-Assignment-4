#!/usr/bin/perl

use strict;
use CGI ':standard';

$file = '../databases/members.csv';



sub checkUsernameExistence {
  open(INFO, "<$file");
  @lines = <INFO>;
  close(INFO);

  foreach $line (@lines) {
    #print "$line";

    @words = split(/\s+/, $line);

    if (@words[0] eq @_[0]) {
      print "Found user\n";
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
  $x = checkUsernameExistence("klk");

  if ($x == 0) {
    writeNewUserToDB("people", "hey");
  }

  $query = $ENV(QUERY_STRING);

  print "Content-Type:text/html;charset=iso-8859-1";
  print "<TITLE>$query</TITLE>";
}

main();

