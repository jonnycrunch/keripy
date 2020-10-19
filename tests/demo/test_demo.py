# -*- encoding: utf-8 -*-
"""
tests.db.dbing module

"""
import pytest

import os

from hio.base import doing
from hio.core.tcp import clienting, serving

from keri.demo import demoing, directing
from keri.db import dbing
from keri.core import eventing, coring


class BobDirector(directing.Director):
    """
    Direct Mode KERI Director (Contextor, Doer) with TCP Client and Kevery
    Generator logic is to iterate through initiation of events for demo

    Inherited Attributes:
        .hab is Habitat instance of local controller's context
        .client is TCP client instance. Assumes operated by another doer.
        .kevery is Kevery instance


    Attributes:

    Inherited Properties:
        .tyme is float relative cycle time, .tyme is artificial time
        .tock is desired time in seconds between runs or until next run,
                 non negative, zero means run asap

    Properties:

    Inherited Methods:
        .__call__ makes instance callable return generator
        .do is generator function returns generator

    Methods:

    Hidden:
       ._tymist is Tymist instance reference
       ._tock is hidden attribute for .tock property
    """


    def do(self, tymist, tock=0.0):
        """
        Generator method to run this doer
        Calling this method returns generator
        """
        try:
            # enter context
            self.wind(tymist)  # change tymist and dependencies
            self.tock = tock
            tyme = self.tyme

            # recur context
            tyme = (yield (tock))  # yields tock then waits for next send

            esn = 0
            counter = coring.SigCounter()  # default is count = 1
            # sign serialization, returns Siger if index provided
            siger = self.hab.signers[esn].sign(self.hab.inception.raw, index=0)
            #  create serialized message
            msg = bytearray(self.hab.inception.raw)
            msg.extend(counter.qb64b)
            msg.extend(siger.qb64b)

            # check valid by creating own Kever using own Kevery
            self.kevery.processOne(ims=bytearray(msg))  # copy of msg
            kever = self.kevery.kevers[self.hab.pre]
            assert kever.prefixer.qb64 == self.hab.pre

            # send to connected remote
            self.client.tx(bytes(msg))  # make copy for now fix later
            del msg[:]  #  clear msg

            tyme = (yield (tock))



        except GeneratorExit:  # close context, forced exit due to .close
            pass

        except Exception:  # abort context, forced exit due to uncaught exception
            raise

        finally:  # exit context,  unforced exit due to normal exit of try
            pass

        return True # return value of yield from, or yield ex.value of StopIteration


class EveDirector(directing.Director):
    """
    Direct Mode KERI Director (Contextor, Doer) with TCP Client and Kevery
    Generator logic is to iterate through initiation of events for demo

    Inherited Attributes:
        .hab is Habitat instance of local controller's context
        .client is TCP client instance. Assumes operated by another doer.
        .kevery is Kevery instance


    Attributes:

    Inherited Properties:
        .tyme is float relative cycle time, .tyme is artificial time
        .tock is desired time in seconds between runs or until next run,
                 non negative, zero means run asap

    Properties:

    Inherited Methods:
        .__call__ makes instance callable return generator
        .do is generator function returns generator

    Methods:

    Hidden:
       ._tymist is Tymist instance reference
       ._tock is hidden attribute for .tock property
    """


    def do(self, tymist, tock=0.0):
        """
        Generator method to run this doer
        Calling this method returns generator
        """
        try:
            # enter context
            self.wind(tymist)  # change tymist and dependencies
            self.tock = tock
            tyme = self.tyme

            # recur context
            tyme = (yield (tock))  # yields tock then waits for next send

            esn = 0
            counter = coring.SigCounter()  # default is count = 1
            # sign serialization, returns Siger if index provided
            siger = self.hab.signers[esn].sign(self.hab.inception.raw, index=0)
            #  create serialized message
            msg = bytearray(self.hab.inception.raw)
            msg.extend(counter.qb64b)
            msg.extend(siger.qb64b)

            # check valid by creating own Kever using own Kevery
            self.kevery.processOne(ims=bytearray(msg))  # copy of msg
            kever = self.kevery.kevers[self.hab.pre]
            assert kever.prefixer.qb64 == self.hab.pre


            tyme = (yield (tock))



        except GeneratorExit:  # close context, forced exit due to .close
            pass

        except Exception:  # abort context, forced exit due to uncaught exception
            raise

        finally:  # exit context,  unforced exit due to normal exit of try
            pass

        return True # return value of yield from, or yield ex.value of StopIteration



def test_directing_basic():
    """
    Test direct mode demo


    """
    # set of secrets  (seeds for private keys)
    bobSecrets = [
                'ArwXoACJgOleVZ2PY7kXn7rA0II0mHYDhc6WrBH8fDAc',
                'A6zz7M08-HQSFq92sJ8KJOT2cZ47x7pXFQLPB0pckB3Q',
                'AcwFTk-wgk3ZT2buPRIbK-zxgPx-TKbaegQvPEivN90Y',
                'Alntkt3u6dDgiQxTATr01dy8M72uuaZEf9eTdM-70Gk8',
                'A1-QxDkso9-MR1A8rZz_Naw6fgaAtayda8hrbkRVVu1E',
                'AKuYMe09COczwf2nIoD5AE119n7GLFOVFlNLxZcKuswc',
                'AxFfJTcSuEE11FINfXMqWttkZGnUZ8KaREhrnyAXTsjw',
                'ALq-w1UKkdrppwZzGTtz4PWYEeWm0-sDHzOv5sq96xJY'
                ]

    #  create bob signers
    bobSigners = [coring.Signer(qb64=secret) for secret in bobSecrets]
    assert [signer.qb64 for signer in bobSigners] == bobSecrets

    # bob inception transferable (nxt digest not empty)
    bobSerder = eventing.incept(keys=[bobSigners[0].verfer.qb64],
                                nxt=coring.Nexter(keys=[bobSigners[1].verfer.qb64]).qb64,
                                code=coring.CryOneDex.Blake3_256)

    bob = bobSerder.ked['pre']
    assert bob == 'ETT9n-TCGn8XfkGkcNeNmZgdZSwHPLyDsojFXotBXdSo'


    # set of secrets (seeds for private keys)
    eveSecrets = ['AgjD4nRlycmM5cPcAkfOATAp8wVldRsnc9f1tiwctXlw',
                  'AKUotEE0eAheKdDJh9QvNmSEmO_bjIav8V_GmctGpuCQ',
                  'AK-nVhMMJciMPvmF5VZE_9H-nhrgng9aJWf7_UHPtRNM',
                  'AT2cx-P5YUjIw_SLCHQ0pqoBWGk9s4N1brD-4pD_ANbs',
                  'Ap5waegfnuP6ezC18w7jQiPyQwYYsp9Yv9rYMlKAYL8k',
                  'Aqlc_FWWrxpxCo7R12uIz_Y2pHUH2prHx1kjghPa8jT8',
                  'AagumsL8FeGES7tYcnr_5oN6qcwJzZfLKxoniKUpG4qc',
                  'ADW3o9m3udwEf0aoOdZLLJdf1aylokP0lwwI_M2J9h0s']

    #  create eve signers
    eveSigners = [coring.Signer(qb64=secret) for secret in eveSecrets]
    assert [signer.qb64 for signer in eveSigners] == eveSecrets

    # eve inception transferable (nxt digest not empty)
    eveSerder = eventing.incept(keys=[eveSigners[0].verfer.qb64],
                                nxt=coring.Nexter(keys=[eveSigners[1].verfer.qb64]).qb64,
                                code=coring.CryOneDex.Blake3_256)

    eve = eveSerder.ked['pre']
    assert eve == 'EwBwUb2eZcA5GDcN7g-87wpreM0nNkLqzkwviBHTcV1A'



    with dbing.openLogger(name="eve") as eveDB, \
         dbing.openLogger(name="bob") as bobDB:

        bobPort = 5620  # bob's TCP listening port for server
        evePort = 5621  # eve's TCP listneing port for server
        bobKevers = dict()
        eveKevers = dict()

        # setup bob
        bobHab = directing.Habitat(secrets=bobSecrets, kevers=bobKevers, db=bobDB)
        assert bobHab.db == bobDB
        assert ([signer.verfer.qb64 for signer in bobHab.signers] ==
                [signer.verfer.qb64 for signer in bobSigners])
        assert bobHab.inception.dig == bobSerder.dig
        assert bobHab.pre == bob

        bobClient = clienting.Client(host='127.0.0.1', port=evePort)
        bobClientDoer = doing.ClientDoer(client=bobClient)

        bobDirector = directing.Director(hab=bobHab, client=bobClient)
        assert bobDirector.hab == bobHab
        assert bobDirector.client == bobClient
        assert bobDirector.kevery.kevers == bobKevers
        assert bobDirector.kevery.logger == bobDB

        bobReactor = directing.Reactor(hab=bobHab, client=bobClient)
        assert bobReactor.hab == bobHab
        assert bobReactor.client == bobClient
        assert bobReactor.kevery.kevers == bobKevers
        assert bobReactor.kevery.logger == bobDB
        assert bobReactor.kevery.ims == bobReactor.client.rxbs

        bobServer = serving.Server(host="", port=bobPort)
        bobServerDoer = doing.ServerDoer(server=bobServer)

        bobDirectant = directing.Directant(hab=bobHab, server=bobServer)
        assert bobDirectant.hab == bobHab
        assert bobDirectant.server == bobServer
        # Bob's Reactants created on demand

        # setup eve
        eveHab = directing.Habitat(secrets=eveSecrets, kevers=eveKevers, db=eveDB)
        assert eveHab.db == eveDB
        assert ([signer.verfer.qb64 for signer in eveHab.signers] ==
                    [signer.verfer.qb64 for signer in eveSigners])
        assert eveHab.inception.dig == eveSerder.dig
        assert eveHab.pre == eve

        eveClient = clienting.Client(host='127.0.0.1', port=bobPort)
        eveClientDoer = doing.ClientDoer(client=eveClient)

        eveDirector = directing.Director(hab=eveHab, client=eveClient)
        assert eveDirector.hab == eveHab
        assert eveDirector.client == eveClient
        assert eveDirector.kevery.kevers == eveKevers
        assert eveDirector.kevery.logger == eveDB

        eveReactor = directing.Reactor(hab=eveHab, client=eveClient)
        assert eveReactor.hab == eveHab
        assert eveReactor.client == eveClient
        assert eveReactor.kevery.kevers == eveKevers
        assert eveReactor.kevery.logger == eveDB
        assert eveReactor.kevery.ims == eveReactor.client.rxbs

        eveServer = serving.Server(host="", port=evePort)
        eveServerDoer = doing.ServerDoer(server=eveServer)

        eveDirectant = directing.Directant(hab=eveHab, server=eveServer)
        assert eveDirectant.hab == eveHab
        assert eveDirectant.server == eveServer
        # Eve's Reactants created on demand



        limit = 0.25
        tock = 0.03125
        doist = doing.Doist(limit=limit, tock=tock)

        bobMsgTx = b"Hi Eve I am  Bob"
        bobDirector.client.tx(bobMsgTx)

        eveMsgTx = b"Hi Bob its me Eve"
        eveDirector.client.tx(eveMsgTx)

        doers = [bobClientDoer, bobDirector, bobReactor, bobServerDoer, bobDirectant,
                 eveClientDoer, eveDirector, eveReactor, eveServerDoer, eveDirectant]
        doist.do(doers=doers)
        assert doist.tyme == limit

        assert bobClient.opened == False
        assert bobServer.opened == False
        assert eveClient.opened == False
        assert eveServer.opened == False

        assert not bobClient.txes
        ca, ix = list(eveServer.ixes.items())[0]
        eveMsgRx = bytes(ix.rxbs)
        assert eveMsgRx == bobMsgTx


        assert not eveClient.txes
        ca, ix = list(bobServer.ixes.items())[0]
        bobMsgRx = bytes(ix.rxbs)
        assert bobMsgRx == eveMsgTx

    assert not os.path.exists(eveDB.path)
    assert not os.path.exists(bobDB.path)
    """End Test"""

def test_direct_mode():
    """
    Test direct mode demo


    """
    # set of secrets  (seeds for private keys)
    bobSecrets = [
                'ArwXoACJgOleVZ2PY7kXn7rA0II0mHYDhc6WrBH8fDAc',
                'A6zz7M08-HQSFq92sJ8KJOT2cZ47x7pXFQLPB0pckB3Q',
                'AcwFTk-wgk3ZT2buPRIbK-zxgPx-TKbaegQvPEivN90Y',
                'Alntkt3u6dDgiQxTATr01dy8M72uuaZEf9eTdM-70Gk8',
                'A1-QxDkso9-MR1A8rZz_Naw6fgaAtayda8hrbkRVVu1E',
                'AKuYMe09COczwf2nIoD5AE119n7GLFOVFlNLxZcKuswc',
                'AxFfJTcSuEE11FINfXMqWttkZGnUZ8KaREhrnyAXTsjw',
                'ALq-w1UKkdrppwZzGTtz4PWYEeWm0-sDHzOv5sq96xJY'
                ]

    #  create bob signers
    bobSigners = [coring.Signer(qb64=secret) for secret in bobSecrets]
    assert [signer.qb64 for signer in bobSigners] == bobSecrets

    # bob inception transferable (nxt digest not empty)
    bobSerder = eventing.incept(keys=[bobSigners[0].verfer.qb64],
                                nxt=coring.Nexter(keys=[bobSigners[1].verfer.qb64]).qb64,
                                code=coring.CryOneDex.Blake3_256)

    bob = bobSerder.ked['pre']
    assert bob == 'ETT9n-TCGn8XfkGkcNeNmZgdZSwHPLyDsojFXotBXdSo'


    # set of secrets (seeds for private keys)
    eveSecrets = ['AgjD4nRlycmM5cPcAkfOATAp8wVldRsnc9f1tiwctXlw',
                  'AKUotEE0eAheKdDJh9QvNmSEmO_bjIav8V_GmctGpuCQ',
                  'AK-nVhMMJciMPvmF5VZE_9H-nhrgng9aJWf7_UHPtRNM',
                  'AT2cx-P5YUjIw_SLCHQ0pqoBWGk9s4N1brD-4pD_ANbs',
                  'Ap5waegfnuP6ezC18w7jQiPyQwYYsp9Yv9rYMlKAYL8k',
                  'Aqlc_FWWrxpxCo7R12uIz_Y2pHUH2prHx1kjghPa8jT8',
                  'AagumsL8FeGES7tYcnr_5oN6qcwJzZfLKxoniKUpG4qc',
                  'ADW3o9m3udwEf0aoOdZLLJdf1aylokP0lwwI_M2J9h0s']

    #  create eve signers
    eveSigners = [coring.Signer(qb64=secret) for secret in eveSecrets]
    assert [signer.qb64 for signer in eveSigners] == eveSecrets

    # eve inception transferable (nxt digest not empty)
    eveSerder = eventing.incept(keys=[eveSigners[0].verfer.qb64],
                                nxt=coring.Nexter(keys=[eveSigners[1].verfer.qb64]).qb64,
                                code=coring.CryOneDex.Blake3_256)

    eve = eveSerder.ked['pre']
    assert eve == 'EwBwUb2eZcA5GDcN7g-87wpreM0nNkLqzkwviBHTcV1A'



    with dbing.openLogger(name="eve") as eveDB, \
         dbing.openLogger(name="bob") as bobDB:

        bobPort = 5620  # bob's TCP listening port for server
        evePort = 5621  # eve's TCP listneing port for server
        bobKevers = dict()
        eveKevers = dict()

        # setup bob
        bobHab = directing.Habitat(secrets=bobSecrets, kevers=bobKevers, db=bobDB)
        assert bobHab.db == bobDB
        assert ([signer.verfer.qb64 for signer in bobHab.signers] ==
                [signer.verfer.qb64 for signer in bobSigners])
        assert bobHab.inception.dig == bobSerder.dig
        assert bobHab.pre == bob

        bobClient = clienting.Client(host='127.0.0.1', port=evePort)
        bobClientDoer = doing.ClientDoer(client=bobClient)

        bobDirector = BobDirector(hab=bobHab, client=bobClient)
        assert bobDirector.hab == bobHab
        assert bobDirector.client == bobClient
        assert bobDirector.kevery.kevers == bobKevers
        assert bobDirector.kevery.logger == bobDB

        bobReactor = directing.Reactor(hab=bobHab, client=bobClient)
        assert bobReactor.hab == bobHab
        assert bobReactor.client == bobClient
        assert bobReactor.kevery.kevers == bobKevers
        assert bobReactor.kevery.logger == bobDB
        assert bobReactor.kevery.ims == bobReactor.client.rxbs

        bobServer = serving.Server(host="", port=bobPort)
        bobServerDoer = doing.ServerDoer(server=bobServer)

        bobDirectant = directing.Directant(hab=bobHab, server=bobServer)
        assert bobDirectant.hab == bobHab
        assert bobDirectant.server == bobServer
        # Bob's Reactants created on demand

        # setup eve
        eveHab = directing.Habitat(secrets=eveSecrets, kevers=eveKevers, db=eveDB)
        assert eveHab.db == eveDB
        assert ([signer.verfer.qb64 for signer in eveHab.signers] ==
                    [signer.verfer.qb64 for signer in eveSigners])
        assert eveHab.inception.dig == eveSerder.dig
        assert eveHab.pre == eve

        eveClient = clienting.Client(host='127.0.0.1', port=bobPort)
        eveClientDoer = doing.ClientDoer(client=eveClient)

        eveDirector = EveDirector(hab=eveHab, client=eveClient)
        assert eveDirector.hab == eveHab
        assert eveDirector.client == eveClient
        assert eveDirector.kevery.kevers == eveKevers
        assert eveDirector.kevery.logger == eveDB

        eveReactor = directing.Reactor(hab=eveHab, client=eveClient)
        assert eveReactor.hab == eveHab
        assert eveReactor.client == eveClient
        assert eveReactor.kevery.kevers == eveKevers
        assert eveReactor.kevery.logger == eveDB
        assert eveReactor.kevery.ims == eveReactor.client.rxbs

        eveServer = serving.Server(host="", port=evePort)
        eveServerDoer = doing.ServerDoer(server=eveServer)

        eveDirectant = directing.Directant(hab=eveHab, server=eveServer)
        assert eveDirectant.hab == eveHab
        assert eveDirectant.server == eveServer
        # Eve's Reactants created on demand

        limit = 0.25
        tock = 0.03125
        doist = doing.Doist(limit=limit, tock=tock)


        # eveMsgTx = b"Hi Bob its me Eve"
        # eveDirector.client.tx(eveMsgTx)

        doers = [bobClientDoer, bobDirector, bobReactor, bobServerDoer, bobDirectant,
                 eveClientDoer, eveDirector, eveReactor, eveServerDoer, eveDirectant]
        doist.do(doers=doers)
        assert doist.tyme == limit

        assert bobClient.opened == False
        assert bobServer.opened == False
        assert eveClient.opened == False
        assert eveServer.opened == False

        assert bobHab.pre in bobHab.kevers
        assert eveHab.pre in eveHab.kevers

        assert not bobClient.txes
        ca, ix = list(eveServer.ixes.items())[0]
        eveMsgRx = bytes(ix.rxbs)
        assert eveMsgRx == bytearray(b'{"vs":"KERI10JSON0000fb_","pre":"ETT9n-TCGn8XfkGkcNeNmZgdZSwHPLy'
                                     b'DsojFXotBXdSo","sn":"0","ilk":"icp","sith":"1","keys":["DSuhyBcP'
                                     b'ZEZLK-fcw5tzHn2N46wRCG_ZOoeKtWTOunRA"],"nxt":"EGAPkzNZMtX-QiVgbR'
                                     b'byAIZGoXvbGv9IPb0foWTZvI_4","toad":"0","wits":[],"cnfg":[]}-AABA'
                                     b'Atf0OqrkGmK3vdMcS5E3mLxeFh14SbvCNjZnZrxAazgYTemZc1S-Pr0ge9IQuHes'
                                     b'mh8cJncRkef1PgxFavDKqDQ')


        #assert not eveClient.txes
        #ca, ix = list(bobServer.ixes.items())[0]
        #bobMsgRx = bytes(ix.rxbs)
        #assert bobMsgRx == eveMsgTx

    assert not os.path.exists(eveDB.path)
    assert not os.path.exists(bobDB.path)
    """End Test"""



if __name__ == "__main__":
    test_directing_basic()
    test_direct_mode()
