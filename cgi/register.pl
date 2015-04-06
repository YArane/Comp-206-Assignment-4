#!/usr/bin/perl
use Data::Dumper;
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
	foreach my $entry (@userData){
		(my $key, my $value) = split(/=/, $entry);
		$value =~ tr/+/ /;
		$value =~ s/%(..)/pack("C", hex($1))/eg;
		$FORM{$key} = $value; 
	}
		
	return %FORM;
}

sub main {
	#read query from post
	#read(STDIN, my $query, $ENV{'CONTENT_LENGTH'});
	#parse query
	my %userData = parseQuery("username=yarden&password=daniel");

	print "Content-type:text/html\r\n\r\n";
	print "<html>";
	print "<head>";
	print "</head>";
	print "<body>";

	my $x = checkUsernameExistence(%userData{'username'});
	#validate username
	if($x == 0) {
		writeNewUserToDB(%userData{'username'}, %userData{'password'});
		print "<p>Congratz! you successfully created a new account.</p>";
	}else{
		#redirect
		print "<p> %userData{'username'} already exists.</p>"
	}

	print "<a href=\"../index.html\"> go back to login page</a>";
	print "</body>";
}

main();
