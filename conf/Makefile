_default:
	@echo "nothing to make.  try make install"

clean:
	rm -f *.o *.so *.pyc *~
	for d in $(SUBDIRS); do make -s -C $$d clean; done

install:
	@if [ "$(DESTDIR)" = "" ]; then \
		echo " "; \
		echo "ERROR: A destdir is required"; \
		exit 1; \
	fi

	mkdir -p $(DESTDIR)/etc/httpd/conf.d
	install -p -m 644 koji-github-webhook_http.conf $(DESTDIR)/etc/httpd/conf.d/koji-github-webhook.conf

	mkdir -p $(DESTDIR)/etc/koji-github-webhook
	install -p -m 644 koji-github-webhook.conf $(DESTDIR)/etc/koji-github-webhook/koji-github-webhook.conf
