Summary: e-smith module to configure dnscache
%define name e-smith-dnscache
Name: %{name}
%define version 1.0.0
%define release 12
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-dnscache-1.0.0.validateNameServer.patch
Patch1: e-smith-dnscache-1.0.0-dnscacne_servers.patch
Patch2: e-smith-dnscache-1.0.0-dnscacne_forwarder.patch
Patch3: e-smith-dnscache-1.0.0-sigpipe.patch
Patch4: e-smith-dnscache-1.0.0-cachesize.patch
Patch5: e-smith-dnscache-1.0.0-reverse_delegation.patch
Patch6: e-smith-dnscache-1.0.0.validateNameServer.patch2
Patch7: e-smith-dnscache-1.0.0-L.root.patch
Patch8: e-smith-dnscache-1.0.0-dnscacne_forwarder.randomseed.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-lib >= 1.15.1-19
Requires: djbdns
BuildRequires: e-smith-devtools
AutoReqProv: no

%description
e-smith server enhancement to configure and run dnscache as a
caching nameserver

%changelog
* Fri Aug 08 2008 Charlie Brady <charlie_brady@mitel.com> 1.0.0-12
- Ensure that forwarding instance of dnscache has random data
  available on stdin. [SME: 4416]

* Wed Jun 18 2008 Charlie Brady <charlie_brady@mitel.com> 1.0.0-11
- Use new address for L root server, and delete included version of
  root/servers/@ file, since we template it. [SME: 4414]

* Wed Jun 18 2008 Charlie Brady <charlie_brady@mitel.com> 1.0.0-10
- Fix validation of NameServer properties pulled from networks db.
  [SME: 1343]

* Wed Jun 18 2008 Charlie Brady <charlie_brady@mitel.com> 1.0.0-9
- Fix delegation of reverse lookup for nets which aren't /8,
  /16 or /24. [SME: 4249]

* Tue Oct 16 2007 Charlie Brady <charlie_brady@mitel.com> 1.0.0-08
- Increase default CacheSize to 10M, with corresponding increase
  in DataSize. [SME: 2371]

* Thu Sep  6 2007 Charlie Brady <charlie_brady@mitel.com> 1.0.0-07
- Run dnscache with sigpipe ignored. [SME: 938]

* Mon May 21 2007 Shad L. Lords <slords@mail.com> 1.0.0-6
- Ensure Forwarder has value and not just defined [SME: 3013]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Fri Apr 06 2007 Shad L. Lords <slords@mail.com> 1.0.0-5
- Fix dnscache root server files [SME: 2721]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Sun Jul 16 2006 Charlie Brady <charlie_brady@mitel.com> 1.0.0-03
- Make dnslog user creation consistent with e-smith-tinydns. [SME: 1688]

* Sun Apr 30 2006 Charlie Brady <charlie_brady@mitel.com> 1.0.0-02
- Don't use NameServer property from networks database if it would
  cause feedback loop. [SME: 1343]

* Thu Mar 16 2006 Charlie Brady <charlie_brady@mitel.com> 1.0.0-01
- Roll (proper) stable stream version. [SME: 1016]

* Tue Mar 14 2006 Charlie Brady <charlie_brady@mitel.com> 0.6.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 0.5.1-06
- Bump release number only

* Thu Oct 27 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.1-05]
- Add default name server delegation for domains without a Nameservers property.
  [SF: 1339875]

* Mon Sep 19 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.1-04]
- Add missing dnscache.forwarder config db record. [SF: 1290325]

* Thu Sep 15 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.1-03]
- Expand templates and restart dnscache.forwarder in dns-update and console-save
  events. Expand templates in bootstrap-console-save rather than
  post-{install,upgrade} events. [SF: 1290325]
- Add support for Forwarder2 property in template for root/servers/@ of
  dnscache.forwarder service.

* Thu Aug 25 2005 Gordon Rowell <gordonr@gormand.com.au>
- [0.5.1-02]
- Configure DNS servers for domains, depending on Nameservers
  property:
  - localhost: 127.0.0.1
  - corporate: dnscache{Forwarder}, dnscache{Forwarder2}
  - internet:  <nothing>
  - Comma separated list of IPs : To those listed servers
- Add dns-update event and reconfigure dnscache there
- Call initialise-default-databases in dns-update to cater for
  domain db migration which might be required due to modification
  of the Corporate DNS Servers
- Migrate db and reconfigure dnscache in domain-modify as well, 
  since we might have changed nameservers.

* Thu Aug 25 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.1-01]
- Roll new development stream prior to reworking Nameservers settings - 0.5.1

* Tue Aug  2 2005 Shad Lords <slords@email.com>
- [0.5.0-23]
- Add TCPPort/UDPPort/access properties to dnscache [SF: 1246986]
- Add COPYING file to distribution

* Wed Jul  6 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-22]
- Only delegate domains if SystemPrimaryDomain or if NameServer
  property is defined. [SF: 1233662]

* Mon Jun  6 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-21]
- Add dnscache log file analysis script
  (from http://www.hungry.com/~fn/dnscache-log.pl.txt).

* Mon Jun  6 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-20]
- Update ICANN root hint name server address list
  (s/128.9.0.107/192.228.79.201/). The 128.9.0.107 address will continue
  answering queries until Jan, 2006.

* Fri May 13 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-19]
- Fix forwarder run script so that logs are captured.

* Mon May  9 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-18]
- Expand dnscache.forwarder service's config in post-install and post-upgrade.

* Thu May  5 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-17]
- Fix problem with migration of legacy Forwarder properties (type
  not specified).

* Tue Apr 26 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-16]
- Really fix creation of root/ip/127 access list file (i.e. put it
  in the correct place).

* Tue Apr 26 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-15]
- Fix creation of ip/127 access list file.

* Wed Apr 20 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-14]
- Create ip/127 access allow file for dnscache.forwarder service.

* Wed Apr 20 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-13]
- Adding missing execute permission on new run scripts.
- Fix errors in config template for forwarding dnscache.

* Wed Apr 20 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-12]
- Add missing /service symlink from previous change.

* Wed Apr 20 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-11]
- Add missing file tree from previous change.

* Wed Apr 20 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-10]
- Add second dnscache instance which does all Internet queries.
  We run the first instance with a small cache, which we
  can happily lose whenever we might have changed any delegations.

* Mon Apr 11 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-09]
- Fix bug in delegation of local networks with NameServer
  property.
- Fix bug in access list configuration.

* Tue Apr  5 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-08]
- Avoid chdir in run script.
- Allow delegation to an alternative listen address for tinydns.
- Avoid unnecessary delegation for 127.in-addr.arpa.

* Wed Mar 30 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-07]
- Fix pathname to root/servers/@ file in createlinks.

* Wed Mar 30 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-06]
- Fix a few deficiencies with new perl run script.

* Wed Mar 30 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-05]
- Use perl run script which does all env setup, access control and zone
  delegation without any templates.

* Wed Mar 30 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-04]
- Fix delegation of reverse lookup of local network. [MN00062867]
- Use generic_template_expand and adjust-services actions in place of
  dnscache-conf. Update e-smith-lib dependency. [MN00064130, MN00065576]
- Update genfilelist call and move to install section.

* Wed Feb 23 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-03]
- Don't run dnscache-conf at post-install, when $LocalIP is undefined.
  [MN00065717]

* Tue Feb 22 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-02]
- Remove any left-behind env/FORWARDONLY file in post scriptlet, so we can
  later simplify config. [charlieb MN00045628]
- Don't attempt to configure dnscache in post-install and post-upgrade.
  [MN00065717]
- Only delegate reverse name lookup when we know of a suitable
  name server. [MN00062867]

* Fri Jan 21 2005 Charlie Brady <charlieb@e-smith.com>
- [0.5.0-01]
- Changing version to development stream number - 0.5.0

* Tue Jan  4 2005 Michael Soulier <msoulier@e-smith.com>
- [0.4.0-01]
- rolling to stable - 0.4.0

* Thu Oct 21 2004 Charlie Brady <charlieb@e-smith.com>
- [0.3.0-04]
- Be sure to remove any left-behind env/FORWARDONLY file. [charlieb MN00045628]

* Thu Aug 26 2004 Michael Soulier <msoulier@e-smith.com>
- [0.3.0-03]
- Updated dnscache-conf for last change. [msoulier MN00045628]

* Thu Aug 26 2004 Michael Soulier <msoulier@e-smith.com>
- [0.3.0-02]
- Updated to handle FORWARDONLY env var properly, to prevent unwanted requests
  for recursion. [msoulier MN00045628]

* Thu Aug 26 2004 Michael Soulier <msoulier@e-smith.com>
- [0.3.0-01]
- rolling to dev - 0.3.0

* Wed Aug 27 2003 Michael Soulier <msoulier@e-smith.com>
- [0.2.0-05]
- Updated the shutdown ordering, and added runlevel 1. [msoulier 9761]

* Mon Aug 25 2003 Michael Soulier <msoulier@e-smith.com>
- [0.2.0-04]
- Moved the rc7 symlink creation to createlinks. [msoulier 9761]

* Mon Aug 25 2003 Michael Soulier <msoulier@e-smith.com>
- [0.2.0-03]
- Added K* script links for runlevels 0 and 6 for dnscache. [msoulier 9761]

* Tue Jul 15 2003 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-02]
- Remove bogus "Requires: supervise-scripts". [charlieb 9448]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-01]
- Changing version to stable stream number - 0.2.0

* Tue Jun 17 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-21]
- Fix restart of dnscache. [charlieb 8745]

* Fri Jun 13 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-20]
- Restart dnscache except after configuration is complete, except for
  certain events (when dnscache will not be running). [gordonr 6762]
- If forwarder is enabled, don't delegate any lookups to local tinydns.
  [charlieb 9032]
- Change Forwarder1 property to Forwarder. Do migration of legacy values here -
  previously done in fragment in e-smith-base RPM.  [charlieb 9032]

* Fri Jun  6 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-19]
- Add "down" file so that dnscache does not start until rc7.d script
  runs. [charlieb 8745]

* Wed Jun  4 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-18]
- Use create-system-user in %pre to create required users. [charlieb 6033]

* Mon Apr 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.8-17]
- Add template for servers/@ and handle DNS forwarders [gordonr 8179]
- Modify template for env/FORWARDONLY to handle DNS forwarders [gordonr 8179]
- Restart dnscache in console-save in case we just changed forwarding
  policy [gordonr 8179]

* Mon Apr  7 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-16]
- Well, it would help if the rc7.d symlink were named correctly. [charlieb 4085]

* Tue Apr  1 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-15]
- Add rc7.d script so that dnscache comes up at boot time. [charlieb 4058]

* Thu Mar 27 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-14]
- Add/delete dnscache delegations for off-site domains/networks if we
  know about them. [charlieb 7845]

* Thu Mar 13 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-13]
- Add default db fragments to defaults, not default :-) [charlieb 7632]

* Tue Mar 11 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-12]
- Add default db fragments, so dnscache is enabled by default.
  Updated e-smithlib dependency. [charlieb 7632]

* Thu Jan 30 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-11]
- Replace Copyright header in spec file with "License: GPL". [charlieb]
- Add /etc/resolv.conf template nameserver fragment. Corresponding
  fragment must be removed from e-smith-base. [charlieb 4058].
- Remove debugging print from dnscache-conf. [charlieb 4058]
- Add 127.in-addr.arpa file - it is constant. [charlieb 4058]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.8-10]
- Updated address for J.ROOT-SERVERS.NET [gordonr 5530]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.8-09]
- Skip servers/@ in dnscache-conf - the root name servers :-) [gordonr 4058]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.8-08]
- Add service domain delegation [gordonr 4058]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.8-07]
- Delegate domain-remote entries to the server defined in the
  Server property of that record.
- Don't delegate remote subnets to the local nameserver - just
  skip them for now [gordonr 4058]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.8-06]
- Wrong bug number last time
- Standardised log/run script with mailfront/qmail/etc. [gordonr 4058]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.8-05]
- Standardised log/run script with mailfront/qmail/etc. [gordonr 6365]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.8-04]
- Call dnscache-conf in post-{install,upgrade} - we need this running
  from the start, even if we need to change details after the bootstrap
  console [gordonr 6365]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.8-03]
- Add missing pipe in genfilelist call so sticky bit preserverved
  on /var/service/dnscache [gordonr 4058]

* Tue Dec  3 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-02]
- Add sticky bit to dnscache service directory, so that svscan starts logging.
- Create /service symlink, so that supervise of dnscache is started by svscan.
  [charlieb 4058]

* Thu Nov 21 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.8-01]
- Rebuild to catch the createlinks update missed by last co2rpm build to 0.1.8

* Thu Nov 21 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.7-02]
- Added root/servers/@ file - we will need to update this some time, as the
  list recently changed.
- Rewrote conf-dnscache to use new DB access classes. Renamed to dnscache-conf.
- Add conf-dnscache links to domain-create and domain-delete events.
- Use links for acl files and delegation files.
- Add code to do local domain delegation (to tinydns).
- We currently do lame delegation for local networks reverse lookup. We
  need to fix this, but currently can't do any better - we don't know any
  name servers for those reverse domains.
- Add sticky bit to dnscache service directory
- Hide output of "id" in %pre script.
  [charlieb 4058]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.7-01]
- RPM rebuild forced by cvsroot2rpm

* Mon Apr  8 2002 Michael Schwern <schwern@e-smith.com>
- [0.1.6-01]
- Update access list manipulation to handle arbitrary bitmasks.

* Wed Mar 13 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.4-01]
- Use correct esmith::utils function names for netmask manip stuff
- Remove trailing dot from network prefixes before creating access
  allow files

* Wed Mar 13 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.3-01]
- Allow dnscache/dnslog users to already exist in %pre script
- Remove bogus -g args from useradd commands
- Update conf-dnscache action script to set up permission to
  query dnscache
- Require supervise-scripts

* Wed Mar 13 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.2-01]
- Create dnscache and dnslog users
- Fix path error in conf-dnscache
- Create /var/log/dnscache directory with correct ownership

* Tue Mar 12 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.1-01]
- Initial

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
perl createlinks
mkdir -p root/service
ln -s /var/service/dnscache root/service
ln -s /var/service/dnscache.forwarder root/service
rm -f %{name}-%{version}-%{release}-filelist

touch root/var/service/dnscache/down
mkdir -p root/var/log/dnscache
mkdir -p root/var/log/dnscache.forwarder
mkdir -p root/var/service/dnscache.forwarder/root/ip
touch root/var/service/dnscache.forwarder/root/ip/127


%pre
/sbin/e-smith/create-system-user dnscache 410 \
    "DNScache user" /var/service/dnscache /bin/false
/sbin/e-smith/create-system-user dnslog 411 \
    "DNS log user" /var/log /bin/false

%post
# Remove any left over env/FORWARDONLY file
rm -f /var/service/dnscache/env/FORWARDONLY

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/service/dnscache 'attr(0755,root,root)' \
    --dir /var/service/dnscache/log 'attr(0755,root,root)' \
    --file /var/service/dnscache/run 'attr(0750,root,root)' \
    --file /var/service/dnscache/dnscache-log.pl 'attr(0750,root,root)' \
    --file /var/service/dnscache/log/run 'attr(0750,root,root)' \
    --dir /var/log/dnscache 'attr(02755,dnslog,dnslog)' \
    --dir /var/log/dnscache.forwarder 'attr(02755,dnslog,dnslog)' \
    --file /var/service/dnscache.forwarder/run 'attr(0750,root,root)' \
    --file /var/service/dnscache.forwarder/log/run 'attr(0750,root,root)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
