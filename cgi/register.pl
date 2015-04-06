#!/usr/bin/perl

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


$x = checkUsernameExistence("klk");

if ($x == 0) {
  writeNewUserToDB("people", "hey");
}
