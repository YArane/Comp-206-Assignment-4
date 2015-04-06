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

sub parseQuery{
	my @userData = split(/&/, @_[0]);
	my %FORM;
	foreach my $entry (my $userData){
		(my $key, my $value) = split(/=/, $entry);
		my $value =~ tr/+/ /;
		$value =~ s/%(..)/pack("C", hex($1))/eg;
		$FORM{$key} = $value; 
	}
		
	return %FORM;
}

sub main {
  #my $x = checkUsernameExistence("klk");

  #if ($x == 0) {
 #   writeNewUserToDB("peopfhjsdhjfsle", "hey");
  #}

  read(STDIN, my $query, $ENV{'CONTENT_LENGTH'});
  my %userData = parseQuery($query);

  print "Content-type:text/html\r\n\r\n";
  print "<html>";
  print "<head>";
  print "</head>";
  print "<body>";
  print "<p>query: $query</p>";
  print "<p>about to print!</p>";
print "<p>$userData{username}</p>";
print "<p>$userData{password}</p>";
  print "<p>printed!</p>";
  print "</body>";
  print "</html>";
}

main();

