#
# TODO:
#   - devel package (?)
#   - fix brs
#
Summary:	Free cross-platform real-time strategy gaming engine
Summary(pl):	Darmowy, wieloplatformowy silnik gier strategicznych czasu rzeczywistego
Name:		stratagus
Version:	2.1
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Games
Vendor:		Stratagus Team
Source0:	http://dl.sourceforge.net/stratagus/%{name}-%{version}-src.tar.gz
# Source0-md5:	ff6b2070b66e8847eeed6bedc24ad8bb
Patch0:		%{name}-includepaths.patch
URL:		http://stratagus.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	bzip2-devel
BuildRequires:	flac-devel
BuildRequires:	glibc-devel
BuildRequires:	libmad-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	linux-libc-headers
BuildRequires:	lua50-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stratagus is a free cross-platform real-time strategy gaming engine.
It includes support for playing over the internet/LAN, or playing a
computer opponent. The engine is configurable and can be used to
create games with a wide-range of features specific to your needs. See
the data sets page for a list of current games using the stratagus
engine.

It is highly active in development and usage.

%description -l pl
Stratagus to darmowy, wieloplatformowy silnik gier strategicznych
czasu rzeczywistego. Zawiera obs³ugê grania przez internet lub w sieci
lokalnej, oraz grania przeciwko komputerowi. Silnik jest
konfigurowalny i mo¿e byæ u¿ywany do tworzenia gier o wielu cechach
specyficznych dla naszych potrzeb. Aktualna lista gier u¿ywaj±cych
silnika stratagus znajduje siê na stronie "data sets".

Projekt jest bardzo aktywny pod wzglêdem rozwoju i wykorzystania.

%prep
%setup -q -n %{name}-040702
%patch0 -p1

%build
#%%{__aclocal}
#%%{__autoconf}
%configure \
	--with-opengl \
	--with-x \
	--with-bzip2 \
	--with-ogg \
	--with-mikmod \
	--with-mad \
	--with-flac \
	--with-cdaudio=sdlcd \
	--with-lua
#cdaudio: libcda,sdlcd,cdda,no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install stratagus $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{_bindir}/*
