@ stdcall NPGetCaps(long)
@ stdcall NPLogonNotify(ptr wstr ptr wstr ptr wstr ptr wstr)
@ stdcall NPPasswordChangeNotify(wstr ptr wstr ptr wstr ptr long)
@ stdcall NPAddConnection(ptr wstr wstr)
@ stdcall NPAddConnection3(long ptr wstr wstr long)
@ stdcall NPCancelConnection(wstr long)
@ stdcall NPGetConnection(wstr ptr ptr)
@ stdcall NPOpenEnum(long long long ptr ptr)
@ stdcall NPEnumResource(long ptr ptr ptr)
@ stdcall NPCloseEnum(long)
@ stdcall NPGetResourceParent(ptr ptr ptr)
@ stdcall NPGetResourceInformation(ptr ptr ptr ptr)
@ stdcall NPGetUniversalName(ptr long ptr ptr)
